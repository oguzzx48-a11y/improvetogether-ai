from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import os
import openai

app = FastAPI()
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.get("/")
def home():
    return {"message": "ImproveTogether AI Bot is running!"}

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_message = data.get("message")

    if not user_message:
        return JSONResponse({"error": "Mesaj bulunamadı."}, status_code=400)

    completion = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Sen kişisel gelişim koçusun. Kullanıcılara motive edici, pozitif ve samimi cevaplar ver."},
            {"role": "user", "content": user_message}
        ]
    )

    reply = completion.choices[0].message.content
    return {"reply": reply}
