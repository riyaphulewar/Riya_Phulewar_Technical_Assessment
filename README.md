🚀 Live Demo (Local Setup)

This project runs fully locally:

Frontend
cd frontend
npm install
npm start

Backend
cd backend
uvicorn main:app --reload


Frontend → http://localhost:3000

Backend → http://127.0.0.1:8000

📌 Features Implemented
✔ Drag & Drop Node Creation

Users can drag nodes from the top toolbar into the canvas.

✔ Fully Custom Node Components

Each node uses a clean abstraction with a shared BaseNode UI.

✔ Smooth Edge Connections

React Flow handles drawing, animations, and graph structure.

✔ Real-time Canvas Editing

Users can:

Move nodes

Connect nodes

Delete nodes

Edit node content

✔ Backend DAG Validation

Pipeline is submitted to FastAPI backend which returns:

Node count

Edge count

Whether the graph is a valid DAG

✔ Clean UI / UX

Soft brown/tan theme

Centered submit button

Minimap, controls & grid background

Resizable nodes

✔ Error-free & Fully Functional

All interactions required by the assessment work exactly as expected.

🛠 Tech Stack
Frontend

React

React Flow

Zustand store

JavaScript

CSS

Backend

Python

FastAPI

CORS Middleware

📂 Project Structure
Riya_Phulewar_Technical_Assessment
├── frontend
│   ├── src
│   │   ├── nodes
│   │   │   ├── InputNode.js
│   │   │   ├── OutputNode.js
│   │   │   ├── LLMNode.js
│   │   │   ├── TextNode.js
│   │   │   ├── MathNode.js
│   │   │   ├── LogicNode.js
│   │   │   ├── DelayNode.js
│   │   │   ├── ApiNode.js
│   │   │   └── MergeNode.js
│   │   ├── ui.js
│   │   ├── toolbar.js
│   │   ├── store.js
│   │   ├── submit.js
│   │   ├── index.css
│   │   └── App.js
│   └── package.json
│
└── backend
    ├── main.py
    └── requirements.txt
    
    ⭐ Learning Outcomes

Through this task I practiced:

React Flow node architecture

Zustand global state management

FastAPI routing & validation logic

UI abstraction using BaseNode

Reusable component design

Real-time graph updates

Connecting frontend to backend

Graph/DAG reasoning

📬 Contact

Riya Phulewar
📧 riyaphulewar1804@gmail.com
