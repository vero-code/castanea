# backend/config.py
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY not found in .env file. Please add it.")
genai.configure(api_key=api_key)

# --- Constants for LLM models ---
MODEL_GEMINI_PRO = "gemini-2.5-pro"
MODEL_GEMINI_FLASH = "gemini-2.5-flash"