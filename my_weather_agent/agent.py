import logging
import os

from dotenv import load_dotenv
from google.adk.agents.llm_agent import LlmAgent
from google.adk.tools import google_search

from my_weather_agent.prompt import ROOT_AGENT_INSTRUCTIONS

logging.info("Loading environment variables")
load_dotenv()
logging.info("MODEL: %s", os.getenv("MODEL"))

logging.info("Creating root agent")
root_agent = LlmAgent(
        name="my_weather_agent",
        model=os.getenv("MODEL"),
        instruction=ROOT_AGENT_INSTRUCTIONS,
        tools=[google_search]
    )