import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")  # Safer than hardcoding
MODEL_NAME = "gpt-3.5-turbo"
