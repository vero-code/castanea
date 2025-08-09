# backend/main.py
from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import logging

load_dotenv()
logging.basicConfig(level=logging.INFO)

from .agent import root_agent
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from google.adk.agents.run_config import RunConfig, StreamingMode
from google.genai.types import Content, Part
from .state import TEST_USER_ID

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

APP_NAME = "castanea"
SESSION_ID = "default_session"
session_service = InMemorySessionService()

class AIRequest(BaseModel):
    query: str

@app.get("/")
def read_root():
    return {"message": "Hello Castanea's user!"}

@app.post("/request")
async def request_to_ai(request: AIRequest):
    try:
        runner = Runner(
            agent=root_agent,
            app_name=APP_NAME,
            session_service=session_service
        )

        try:
            await session_service.get_session(APP_NAME, TEST_USER_ID, SESSION_ID)
        except Exception:
            logging.info("Creating a new session.")
            await session_service.create_session(
                app_name=APP_NAME, user_id=TEST_USER_ID, session_id=SESSION_ID
            )

        run_config = RunConfig(streaming_mode=StreamingMode.NONE, max_llm_calls=100)
        content = Content(role="user", parts=[Part(text=request.query)])

        async for event in runner.run_async(
                user_id=TEST_USER_ID,
                session_id=SESSION_ID,
                new_message=content,
                run_config=run_config
        ):
            if event.is_final_response():
                if event.content and event.content.parts:
                    return {"response": event.content.parts[0].text}
                else:
                    logging.error("Final response has no content.")
                    raise HTTPException(status_code=500, detail="Agent returned an empty response.")

        logging.warning("Agent finished run without a final response event.")
        raise HTTPException(status_code=500, detail="No final response from agent.")

    except Exception as e:
        logging.exception(f"An unhandled error occurred in the agent logic: {e}")
        raise HTTPException(status_code=500, detail="Agent failed to process your query.")