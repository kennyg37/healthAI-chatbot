from fastapi import FastAPI
from pydantic import BaseModel
from transformers import GPT2LMHeadModel, AutoTokenizer
import torch
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

CHECKPOINT_PATH = "chatbot_model/checkpoint-174"

# Load tokenizer from the original GPT-2 model
tokenizer = AutoTokenizer.from_pretrained("gpt2")
tokenizer.pad_token = tokenizer.eos_token 

model = GPT2LMHeadModel.from_pretrained(CHECKPOINT_PATH)
model.eval()

class PromptRequest(BaseModel):
    prompt: str

@app.get("/")
def home():
    return {"message": "healtAI chatbot is running!"}

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],
)

@app.post("/generate/")
def generate_text(request: PromptRequest):
    """
    Generates text based on the given prompt.
    Parameters:
        - request (PromptRequest): The request body containing the prompt.
    Returns:
        - Generated text.
    """
    input_text = f"User: {request.prompt}\nBot:"
    input_ids = tokenizer(input_text, return_tensors="pt").input_ids

    # Create attention mask (1 for all tokens since pad_token == eos_token)
    attention_mask = torch.ones(input_ids.shape, device=input_ids.device)

    with torch.no_grad():
        output = model.generate(
            input_ids,
            attention_mask=attention_mask,  # Pass the attention mask here
            max_length=50, 
            do_sample=True, 
            temperature=0.7, 
            top_k=50,  
            top_p=0.9,  
            repetition_penalty=1.2,  
            no_repeat_ngram_size=4,  
            pad_token_id=tokenizer.eos_token_id,
            eos_token_id=tokenizer.eos_token_id
        )

    # Decode the response
    response = tokenizer.decode(output[:, input_ids.shape[-1]:][0], skip_special_tokens=True)
    return {"bot": response}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)