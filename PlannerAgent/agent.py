import logging
import os

from dotenv import load_dotenv
from google.adk.agents.llm_agent import LlmAgent
from google.adk.tools import google_search

from PlannerAgent import prompt

logging.info("Loading environment variables")
load_dotenv()


async def idea_tool(user_input: str) -> str:
    """
    Generates creative and exciting weekend travel ideas based on the user's budget & destination
    """
    return "Here are some ideas for your weekend trip: \n1. Visit the local art gallery \n2. Go hiking in the nearby mountains \n3. Have a picnic in the park"

async def refiner_tool(user_input: str, idea: str) -> str:
    """
    Refines the provided travel ideas and selects only those that are within the user's budget
    """
    return "Here are the refined ideas for your weekend trip: \n1. Visit the local art gallery \n2. Go hiking in the nearby mountains \n3. Have a picnic in the park"


idea_agent = LlmAgent(
        name="IdeaAgent",
        model=os.getenv("MODEL"),
        description="Brainstorms creative and exciting weekend travel ideas based on the user's budget & destination using available tools",
        instruction=prompt.IDEA_AGENT_INSTRUCTIONS,
        tools=[idea_tool],
        disallow_transfer_to_peers=True,
    )

refiner_agent = LlmAgent(
        name="RefinerAgent",
        model=os.getenv("MODEL"),
        description="Reviews provided travel ideas from the idea agent and select only those that are within the user's budget using available tools",
        instruction=prompt.REFINER_AGENT_INSTRUCTIONS,
        tools=[refiner_tool],
        disallow_transfer_to_peers=True,
    )    


root_agent = LlmAgent(
        name="PlannerAgent",
        model=os.getenv("MODEL"),
        description="Coordinating specialists agents to provide budget friendly trip ideas",
        instruction=prompt.ROOT_AGENT_INSTRUCTIONS,
        sub_agents=[idea_agent,refiner_agent]
    )