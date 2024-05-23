from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from folders.routers import router as folder_router
from task_status.routers import router as task_status_router
from tasks.routers import router as task_router

app = FastAPI()

origins = [
    "http://localhost:4200",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return """Hello Task Tracker)"""


app.include_router(folder_router)
app.include_router(task_status_router)
app.include_router(task_router)
