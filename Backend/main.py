from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from database import (
    create_conversation,
    conversation_exists,
    save_message,
    get_conversation_messages,
    get_all_conversations
)

from ai_service import get_ai_answer


app = FastAPI(title="AI Chat Project")


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:5174",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:5174"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class NewConversationRequest(BaseModel):
    title: str = "New chat"


class ChatRequest(BaseModel):
    message: str
    conversation_id: int | None = None


@app.get("/api/health")
def health_check():
    return {"status": "ok"}


@app.get("/api/conversations")
def get_conversations():
    return get_all_conversations()


@app.post("/api/conversations")
def start_new_conversation(request: NewConversationRequest):
    title = request.title.strip() if request.title else "New chat"

    if not title:
        title = "New chat"

    conversation_id = create_conversation(title)

    return {
        "conversation_id": conversation_id,
        "title": title
    }


@app.get("/api/conversations/{conversation_id}/messages")
def get_messages(conversation_id: int):
    if not conversation_exists(conversation_id):
        raise HTTPException(status_code=404, detail="Conversation not found")

    return get_conversation_messages(conversation_id)


@app.post("/api/chat")
def chat(request: ChatRequest):
    user_message = request.message.strip()

    if not user_message:
        raise HTTPException(status_code=400, detail="Message cannot be empty")

    conversation_id = request.conversation_id

    # Если conversation_id не пришёл, равен 0, или такой беседы нет — создаём новую.
    if conversation_id is None or conversation_id <= 0 or not conversation_exists(conversation_id):
        title = user_message[:50]
        conversation_id = create_conversation(title)

    save_message(conversation_id, "user", user_message)

    history = get_conversation_messages(conversation_id)

    try:
        assistant_answer = get_ai_answer(history)
    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=f"OpenAI API error: {str(error)}"
        )

    save_message(conversation_id, "assistant", assistant_answer)

    updated_messages = get_conversation_messages(conversation_id)

    return {
        "conversation_id": conversation_id,
        "answer": assistant_answer,
        "messages": updated_messages
    }