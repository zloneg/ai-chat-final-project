# AI Chat Project

Full Stack Web Developer final project.

## Developer

Sofia Kaplan

## Description

AI Chat Project is a full stack web application that allows users to start and continue conversations with an AI assistant.

The user writes a message in the React interface. The frontend sends the message to the FastAPI backend. The backend sends the conversation context to OpenAI API, receives the assistant response, saves both user and assistant messages in MySQL, and returns the answer to the frontend.

## Technologies

- React
- JavaScript
- Python
- FastAPI
- MySQL
- OpenAI API
- Vite
- Axios
- React Router

## Project Structure

```text
Sofia_Kaplan_Final_Project_31.5.26/
│
├── Database/
│   └── ai_chat_project_export.sql
│
├── Backend/
│   ├── main.py
│   ├── database.py
│   ├── ai_service.py
│   ├── requirements.txt
│   ├── .env.example
│   └── postman_collection.json
│
├── Frontend/
│   ├── package.json
│   ├── package-lock.json
│   ├── index.html
│   ├── src/
│   └── vite.config.js
│
├── README.md
└── .gitignore
```

## Main Features

- Start a new AI chat
- Continue the same conversation in context
- Store conversations in MySQL
- Store user and assistant messages in MySQL
- Display user and assistant messages on different sides
- Navigate between Home and About pages
- Use OpenAI API only from the backend
- Keep API key in backend `.env` file

## Backend Routes

```text
GET  /api/health
GET  /api/conversations
POST /api/conversations
GET  /api/conversations/{conversation_id}/messages
POST /api/chat
```

## Database

Database name:

```text
ai_chat_project
```

Tables:

```text
conversations
messages
```

The `conversations` table stores chat sessions.

The `messages` table stores all user and assistant messages and connects them to a specific conversation using `conversation_id`.

## How to Run Backend

Go to the backend folder:

```bash
cd Backend
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file based on `.env.example`.

Run the backend server:

```bash
python -m uvicorn main:app --host 0.0.0.0 --port 4000 --reload
```

Backend Swagger documentation:

```text
http://localhost:4000/docs
```

## How to Run Frontend

Go to the frontend folder:

```bash
cd Frontend
```

Install dependencies:

```bash
npm install
```

Run the frontend:

```bash
npm run dev
```

Frontend URL:

```text
http://localhost:5173
```

## Environment Variables

Create a `.env` file inside the Backend folder based on `.env.example`:

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_mysql_password_here
DB_NAME=ai_chat_project

OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL=gpt-5.5
```

The real `.env` file must not be uploaded to GitHub.

## GitHub

GitHub repository link:

https://github.com/zloneg/ai-chat-final-project.git