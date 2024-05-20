import vertexai
from vertexai.generative_models import GenerativeModel, Part
import google.generativeai as genai
from PIL import Image

from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

api_key = os.getenv("API_KEY")

# Generate text from an image 

def generate_text(image, prompt):
    try:
        API_KEY = api_key
        genai.configure(api_key=API_KEY)

        model = genai.GenerativeModel('gemini-pro-vision')

        # Assuming non-streaming for simplicity
        response = model.generate_content(
                [prompt, image],
                stream=True
            )
        response.resolve()
        if hasattr(response, 'text'):
            return response.text
        else:
            return "No text response available"

    except Exception as e:
        print(f"An error occurred: {e}")
        return None
