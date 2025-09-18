from google.adk.agents import LlmAgent
from pydantic import BaseModel, Field

class EmailInput(BaseModel):
    subject : str = Field(description="The subject of the email")
    body: str = Field(description="The body of the email")
    

root_agent = LlmAgent(
    name="agent",
    description="An agent that can help build a proffesional email with a structured subject and body.",
    model="gemini-2.0-flash-lite",
    instruction="""
        You are email generation agent.
        Your task is to provide a structured email with a subject and body based on the user's request.
        GUIIDELINES:
        - The subject should be concise and relevant to the email content.
        - The body should be clear, professional, and to the point.
        - Use proper grammar and punctuation.
        - Avoid unnecessary jargon or complex language.
        - Ensure the email is polite and respectful.
        - email tone should match the context of the request (formal, informal, etc.).
        - If the user specifies a tone, ensure the email reflects that tone.
        
        IMPORTANT:
        - Always respond in JSON format with the following structure:
        {
            "subject": "Subject of the email",
            "body": "eamil body with proper paragraph and structure",
        }
        
        DO NOT include any explanations or additional text outside the JSON structure.
    """,
    output_schema=EmailInput,
    output_key="email",
)