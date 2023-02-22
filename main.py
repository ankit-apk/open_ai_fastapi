from fastapi import FastAPI
import openai
import os

app = FastAPI()
openai.api_key = os.getenv("OPENAI_KEY")


@app.get("/ask/{question}")
async def ask_question(question: str):
    # create a completion
    completion = openai.Completion.create(
        model="text-davinci-003",
        prompt=question,
        max_tokens=3000,
        temperature=0
    )
    return {"data": completion["choices"][0]["text"]}
