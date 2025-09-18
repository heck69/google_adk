from google.adk.agents import Agent

root_agent = Agent(
    name="question_answering_agent",
    description="An agent that can answer questions based on user preferences stored in the session state.",
    model="gemini-2.0-flash",
    instruction="""
        you are a helpful agent that can answer questions based on user preferences stored in the session state.
        The session state contains information about the user's name and preferences.
        information about the user's name and preferences:
        Name:
        {user_name}
        preferences:
        {user_preferences}
    """,
)