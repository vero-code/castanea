# backend/sub_agents.py
from google.adk.agents import Agent
from .config import MODEL_GEMINI_PRO, MODEL_GEMINI_FLASH
from .tools import perplexity_search, save_report

# --- Sub-Agent Definitions ---

# Agent 1: The Researcher
researcher_agent = Agent(
    name="ResearcherAgent",
    model=MODEL_GEMINI_PRO,
    description="A sophisticated research agent that combines real-time search with advanced synthesis. "
                "It uses Perplexity to gather facts and then its own intelligence to write a comprehensive report.",
    instruction="You are a highly skilled Research Specialist. Your task is to create a detailed report on a given topic "
                "by following a strict two-step process:\n"
                "1. **GATHER:** First, you MUST use the 'perplexity_search' tool to gather raw, up-to-date information "
                "about the user's query. This is your fact-finding phase.\n"
                "2. **SYNTHESIZE:** Second, after you receive the raw text from the tool, you MUST process, analyze, and "
                "restructure that information into a high-quality, well-written, and comprehensive report. Do not simply "
                "output the raw text from the tool. Your value lies in transforming messy data into a polished, "
                "coherent, and easy-to-understand final answer for the student.",
    tools=[perplexity_search],
)

# Agent 2: The Analyst
analyst_agent = Agent(
    name="AnalystAgent",
    model=MODEL_GEMINI_FLASH,
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
    tools=[save_report],
)

sub_agents_list = [
    researcher_agent,
    analyst_agent,
    writer_agent,
]