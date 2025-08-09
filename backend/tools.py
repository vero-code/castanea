# backend/tools.py
import os
import requests
import logging
from dotenv import load_dotenv
from openai import OpenAI

# --- Configuration ---
load_dotenv()
logging.basicConfig(level=logging.INFO)

try:
    client = OpenAI(
        api_key=os.getenv("PERPLEXITY_API_KEY"),
        base_url="https://api.perplexity.ai"
    )
except Exception as e:
    logging.error(f"Failed to initialize OpenAI client for Perplexity: {e}")
    client = None


def perplexity_search(query: str) -> str:
    """
    Performs a search using the Perplexity API via the OpenAI client library.
    This is the primary tool for the ResearcherAgent.

    Args:
        query: The specific question or topic to search for.

    Returns:
        A string containing the answer from Perplexity, or an error message.
    """
    logging.info(f"--- Tool: perplexity_search called with query: '{query}' ---")
    if not client:
        return "Error: Perplexity client was not initialized. Check API key and environment."

    messages = [
        {
            "role": "system",
            "content": "You are a helpful and factual research assistant for a student. Provide clear, well-structured answers.",
        },
        {
            "role": "user",
            "content": query
        }
    ]

    try:
        response = client.chat.completions.create(
            model="sonar-pro",
            messages=messages,
        )

        answer = response.choices[0].message.content
        logging.info("--- Tool: perplexity_search successfully received an answer. ---")
        return answer

    except Exception as e:
        error_msg = f"An error occurred during the Perplexity API call: {e}"
        logging.error(error_msg)
        return error_msg

def save_report(filename: str, content: str) -> str:
    """
    Saves the provided content to a text file in a 'reports' directory.
    This tool can be used by the WriterAgent.

    Args:
        filename: The name of the file (e.g., 'climate_change_essay.txt').
        content: The text content to save.

    Returns:
        A confirmation message.
    """
    logging.info(f"--- Tool: save_report called for filename: '{filename}' ---")
    try:
        # Create a 'reports' directory if it doesn't exist
        if not os.path.exists('reports'):
            os.makedirs('reports')

        filepath = os.path.join('reports', filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        success_msg = f"Successfully saved the report to '{filepath}'."
        logging.info(success_msg)
        return success_msg
    except Exception as e:
        error_msg = f"Failed to save the file: {e}"
        logging.error(error_msg)
        return error_msg