import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

MODEL = os.getenv("OPENAI_MODEL", "gpt-5.5")


def build_conversation_text(history):
    lines = []

    for message in history:
        if message["role"] == "user":
            lines.append(f"User: {message['content']}")
        else:
            lines.append(f"Assistant: {message['content']}")

    return "\n".join(lines)


def get_ai_answer(history):
    conversation_text = build_conversation_text(history)

    response = client.responses.create(
        model=MODEL,
        instructions=(
            "You are a helpful AI assistant. "
            "Answer naturally and keep the context of the current conversation."
        ),
        input=conversation_text
    )

    return response.output_text