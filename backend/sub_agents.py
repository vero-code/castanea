# backend/sub_agents.py
from google.adk.agents import Agent
from .config import MODEL_GEMINI_PRO

# --- Sub-Agent Definitions ---

# Agent 1: The Researcher
researcher_agent = Agent(
    name="ResearcherAgent",
    model=MODEL_GEMINI_PRO,
    description="Handles end-to-end research tasks. Takes a topic, breaks it down, finds information "
                ", and synthesizes a complete, structured report.",
    instruction="You are a Research Specialist. You will receive a topic from the coordinator. "
                "Your task is to perform a full research cycle: \n"
                "1. Deconstruct the topic into logical sub-questions. \n"
                "2. For each sub-question, find detailed information (using your internal knowledge for now). \n"
                "3. Synthesize all findings into a single, cohesive, and well-structured final report. "
                "Return only this final report.",
)

# Agent 2: The Analyst
analyst_agent = Agent(
    name="AnalystAgent",
    model=MODEL_GEMINI_PRO,
    description="Analyzes a given piece of text. It can summarize, extract key points, "
                "identify sentiment, or perform other analytical tasks on existing content.",
    instruction="You are a Data Analyst. You will receive a block of text and a specific instruction "
                "(e.g., 'summarize', 'extract keywords'). Your only job is to perform that specific "
                "analytical task on the provided text and return the result. Do not add any new information.",
)

# Agent 3: The Writer
writer_agent = Agent(
    name="WriterAgent",
    model=MODEL_GEMINI_PRO,
    description="Generates original written content. It can write essays, articles, emails, "
                "reports, or creative pieces based on a user's prompt.",
    instruction="You are a professional Writer. You will receive a prompt asking you to create a specific "
                "type of document (e.g., essay, letter, summary). Your task is to write that document from "
                "scratch, adhering to the user's requirements for tone, style, and content. Return only the "
                "finished written piece.",
)

sub_agents_list = [
    researcher_agent,
    analyst_agent,
    writer_agent,
]