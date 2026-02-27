# Task Manager API

Final project for the backend course. Its a simple REST API built with FastAPI that lets you manage tasks. Nothing fancy, tasks get saved to a plain text file so they dont disappear when you restart the server.


# What it does

-create, read, update and delete tasks (CRUD)
-Filter tasks by completion status
-See stats like total tasks and completion percentage
-Data stays saved even after restarting the server (stored in `tasks.txt`)
-Comes with a simple browser frontend


# Project structure

fastapi-tasks/
├── main.py          # all the API endpoints
├── helpers.py       # functions for reading and writing the file
├── tasks.txt        # where the tasks are saved (JSON Lines)
├── requirements.txt # python packages needed
├── render.yaml      # config for deploying on Render
├── static/
│   └── index.html   # the frontend UI
└── README.md        # this file


# How to run it locally

1. Clone the repo

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME
cd YOUR_REPO_NAME


2. Install dependencies

```bash
pip install -r requirements.txt


3. Start the server

```bash
uvicorn main:app --reload


4. Open in browser

- Frontend UI: http://127.0.0.1:8000
- API docs (Swagger): http://127.0.0.1:8000/docs


# API Endpoints

| Method | URL | Description |
|--------|-----|-------------|
| GET | `/` | Check if API is running |
| GET | `/tasks` | Get all tasks |
| GET | `/tasks?completed=true` | Filter by completion status |
| GET | `/tasks/{id}` | Get a single task |
| POST | `/tasks` | Create a new task |
| PUT | `/tasks/{id}` | Update a task |
| DELETE | `/tasks/{id}` | Delete one task |
| DELETE | `/tasks` | Delete all tasks |
| GET | `/tasks/stats` | Get summary stats |

# Example: Creating a task

```bash
curl -X POST http://127.0.0.1:8000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Learn FastAPI", "description": "Watch the tutorials"}'
```

Response:
```json
{
  "id": 1,
  "title": "Learn FastAPI",
  "description": "Watch the tutorials",
  "completed": false
}


# How tasks are stored

Each task is saved as one JSON object per line in `tasks.txt`:

{"id": 1, "title": "Learn FastAPI", "description": "Watch tutorials", "completed": false}
{"id": 2, "title": "Buy groceries", "description": "Milk and eggs", "completed": true}


# Deploying to Render 

1.Push the code to a public GitHub repo
2.Create a free account on render.com
3.New -> Web Service -> connect your repo
4.It picks up render.yaml on its own and configures everything
5.Hit deploy and wait a minute


# Next steps

-Add PostgreSQL: Replace the text file with a real database. Render offers a free PostgreSQL instance you can connect with SQLModel or SQLAlchemy.

-Add React frontend: Replace the basic HTML frontend with a proper React app.

-Add user authentication: Use JWT tokens so each user has their own tasks.

-Add due dates: Extend the task model with a `due_date` field and sort by urgency.

# Tech used

- [FastAPI](https://fastapi.tiangolo.com/) – the web framework
- [Pydantic](https://docs.pydantic.dev/) – data validation
- [Uvicorn](https://www.uvicorn.org/) – ASGI server
- Vanilla JavaScript – frontend


