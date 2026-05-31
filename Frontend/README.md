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