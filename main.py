from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from service.assist import Assist
from service.question import Question

app = FastAPI()

origins = [
    "http://101.180.165.41:8090"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/ask/")
def ask_question(question: Question):
    assist=Assist()
    response=assist.ask(question.question)
    return {"response": response}
