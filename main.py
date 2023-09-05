import openai
from fastapi import FastAPI

app: FastAPI = FastAPI()
messages = []


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/send_message")
async def send_message(text: str):
    messages.append({"role": "system", "content": text})

    while input != "quit()":
        message = input()
        messages.append({"role": "system", "content": message})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages)
        reply: str = response["choices"][0]["message"]["content"]
    return {"message": reply}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)


