# imports
import os
from dotenv import load_dotenv
from langchain.tools import tool
from langchain.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI

# load env
load_dotenv()

# Initialise agent
agent = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=1.0,  
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # other params...
)

# define system prompt and human message that agent will respond to
messages = [
    (
        "system",
        "You are a helpful girlfriend.",
    ),
    (
        "human", 
        "How are you today?"
    ),
]

ai_msg = agent.invoke(messages)
print(ai_msg)