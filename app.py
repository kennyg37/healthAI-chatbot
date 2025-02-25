from fastapi import FastAPI
from pydantic import BaseModel
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

app = FastAPI()

CHECKPOINT_PATH = "chatbot_model/checkpoint-174"

# Load tokenizer from the original GPT-2 model
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

model = GPT2LMHeadModel.from_pretrained(CHECKPOINT_PATH)
model.eval()

class PromptRequest(BaseModel):
    prompt: str

@app.get("/")
def home():
    return {"message": "healtAI chatbot is running!"}

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

    with torch.no_grad():
        output = model.generate(
            input_ids,
            max_length=50,
            pad_token_id=tokenizer.eos_token_id 
        )

    # Decode the response 
    response = tokenizer.decode(output[:, input_ids.shape[-1]:][0], skip_special_tokens=True)
    return {"bot": response}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)