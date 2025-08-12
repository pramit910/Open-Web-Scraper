# src/main.py
import os
from dotenv import load_dotenv
from gradio_app import create_gradio_app

# Load environment variables from the .env file
load_dotenv()

# Create and launch the Gradio application
if __name__ == "__main__":
    app = create_gradio_app()
    app.launch()
