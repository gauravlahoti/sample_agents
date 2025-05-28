import logging
import os

from dotenv import load_dotenv
from google.adk.agents.llm_agent import LlmAgent
from google.adk.tools import google_search

from PlannerAgent import prompt

logging.info("Loading environment variables")
load_dotenv()


idea_agent = LlmAgent(
        name="IdeaAgent",
        model=os.getenv("MODEL"),
        description="Brainstorms creative and exciting weekend travel ideas based on the user's budget & destination",
        instruction=prompt.IDEA_AGENT_INSTRUCTIONS,
        tools=[google_search],
        disallow_transfer_to_peers=True,
    )

refiner_agent = LlmAgent(
        name="RefinerAgent",
        model=os.getenv("MODEL"),
        description="Reviews provided travel ideas and select only those that are within the user's budget",
        instruction=prompt.REFINER_AGENT_INSTRUCTIONS,
        # tools=[google_search],
        disallow_transfer_to_peers=True,
    )    


root_agent = LlmAgent(
        name="PlannerAgent",
        model=os.getenv("MODEL"),
        description="Coordinating specialists agents to provide budget friendly trip ideas",
        instruction=prompt.ROOT_AGENT_INSTRUCTIONS,
        tools=[google_search],
        # sub_agents=[idea_agent]
    )