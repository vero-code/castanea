# # backend/agent.py
from dotenv import load_dotenv
import logging

from google.adk.agents import Agent
from .config import MODEL_GEMINI_PRO
from .sub_agents import sub_agents_list

# --- Configuration ---
load_dotenv()
logging.basicConfig(level=logging.INFO)

# @title Define the Root Agent (Coordinator)
root_agent = Agent(
    name="CastaneaCoordinator",
    model=MODEL_GEMINI_PRO,
    description="A top-level dispatcher agent. It analyzes the user's request to determine the primary "
                "intent and delegates the entire task to the most suitable specialized sub-agent.",
    instruction="You are the central dispatcher for the Castanea AI platform. Your only job is to analyze the "
                "user's request and delegate it to the single most appropriate specialist agent. **You do not "
                "answer questions or perform tasks yourself.**\n\n"
                "Use the following logic to delegate:\n"
                "- If the user asks a question that requires finding and synthesizing new information, "
                "or asks for a report on a topic (e.g., 'What is quantum entanglement?', 'Tell me about the "
                "history of Rome'), delegate to the **'ResearcherAgent'**.\n"
                "- If the user provides a body of text and asks to perform an action on it (e.g., 'Summarize this "
                "article for me', 'Extract the key points from this text'), delegate to the **'AnalystAgent'**.\n"
                "- If the user asks you to write original content from a prompt, like an essay, a poem, a letter, "
                "or a story (e.g., 'Write an essay about climate change', 'Compose a formal resignation letter'), "
                "delegate to the **'WriterAgent'**.\n\n"
                "Your response should ONLY be the delegation to the correct agent.",
    tools=[],
    sub_agents=sub_agents_list,
)