from google.adk.agents import Agent
from google.adk.tools import google_search
from datetime import datetime

def get_current_time() -> dict:
    """
    get current time in the format of DD-MM-YYYY HH:MM:SS"""
    return {
        "current_time": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    }
    
root_agent = Agent(
    name="agent",
    model = "gemini-2.0-flash-lite",
    description = "tool agent",
    instruction="""
    you are a helpful assistant that can use tools:
    -get_current_time""",
    #tools=[google_search],  
    tools = [get_current_time],  
)