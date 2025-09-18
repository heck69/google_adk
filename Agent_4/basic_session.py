import asyncio  
from google.adk.sessions import InMemorySessionService
from dotenv import load_dotenv
from google.adk.runners import Runner
from google.genai import types
from session.agent import root_agent
import uuid

load_dotenv()
async def main():
    session_service_stateful = InMemorySessionService()

    initial_state = {
        "user_name": "sharan",
        "user_preferences": """
            I like to play badminton, basketbal and cricket.
            My favourite food is biryani.
            My favourite Movie is Salaar-pt1.
            Loves people who are idiots.
        """,
    }

    #Create a new session.
    APP_NAME = "bot"
    USER_ID = "sharan@69"
    SESSION_ID = str(uuid.uuid4())
    stateful_session = await session_service_stateful.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,   
        session_id=SESSION_ID,
        state=initial_state,
    )

    print(f"Stateful session created with ID: {SESSION_ID}")

    runner = Runner(
        agent = root_agent,
        session_service=session_service_stateful,
        app_name=APP_NAME,
    )

    new_message = types.Content(
        role = "user", parts=[types.Part(text ="What is my name?")]
    )

    for event in runner.run(
        session_id=SESSION_ID,
        user_id=USER_ID,
        new_message=new_message,
    ):
        if event.is_final_response:
            if event.content and event.content.parts:
                print(f"Final response: {event.content.parts[0].text}")

    print("=== Session Event Exploration ===")
    session = await session_service_stateful.get_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID,
    )

    print("===FINAL SESSION STATE===")
    for key, value in session.state.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    asyncio.run(main())

