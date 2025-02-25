# HealthAI chatbot

This repository contains a botebook for a chatbot creation and an fastapi api to use the chatbot. The chatbot used pre-trained GPT-2 model which is a transformer model

## Links
- **Demo**: [https://drive.google.com/drive/folders/11LLfRhkvjDD9pEgl7cEPB4ZWVUfwVPzt?usp=sharing](here)
- **Frontend Repo:**: [https://github.com/kennyg37/healthAI-fn.git](frontend link)
- **Report:** [https://docs.google.com/document/d/1bF2Fm2IYAmaho7C8QkZBPdHAYqE8F0TtZK_jPWHwQ0c/edit?usp=sharing](here)

## Repository Structure


## Notebooks

- **File:** [chatbot.ipynb](chatbot.ipynb)
- **Description:** Initial data exploration and preprocessing. Loads the training and test datasets and inspects the first few rows. Then proceeds to create a chatbot that can be used to ask health querries


## Data
- **Training Data:** [data.json](data.json)

## API
- **Api file:** [app.py](app.py)

## Setup
1. Clone the repository.
2. Create a virtual environment:
    ```sh
    python -m venv venv
    ```
3. Activate the virtual environment:
    - On Windows:
        ```sh
        .\venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```
4. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```
5. Run the application:
    ```
    uvicorn app:app --host 0.0.0.0 --port 8000 --reload
    ```


## Usage
Open the Jupyter notebooks in your preferred environment (e.g., Jupyter Lab, Google Colab) and run the cells to reproduce the experiments.

## License
This project is licensed under the MIT License.