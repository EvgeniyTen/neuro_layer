import openai
from fastapi import FastAPI
from aiohttp import ClientSession

app: FastAPI = FastAPI()

class OpenAIService:
    def __init__(self, api_key, model):
        self.messages = []
        openai.api_key = api_key
        self.model = model
        self.system_message = {"role": "system", "content": "You are a helpful assistant"}
        self.temperature = 1.0

    async def send_message(self, text):
        self.messages.append({"role": "user", "content": text})
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=self.messages
        )
        reply = response["choices"][0]["message"]["content"]
        self.messages.append({"role": "assistant", "content": reply})
        return reply

# Configuration
openai_service = OpenAIService(api_key="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",
                               model="gpt-3.5-turbo")




@app.post("/send_message")
async def send_message(text: str):
    try:
        response_text = await openai_service.send_message(text)
        return {"message": response_text}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)


