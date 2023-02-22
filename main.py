from fastapi import FastAPI
import openai

app = FastAPI()


@app.get("/ask/")
async def ask_question(question: str):
    openai.api_key = "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"

    # create a completion
    completion = openai.Completion.create(
        model="text-davinci-003",
        prompt=question,
        max_tokens=3000,
        temperature=0
    )
    return {"data": completion["choices"][0]["text"]}
