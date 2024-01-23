from fastapi import FastAPI

from service.assist import Assist
from service.question import Question

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/ask/")
def ask_question(question: Question):
    assist=Assist()
    response=assist.ask(question.question)
    return {"response": response}
