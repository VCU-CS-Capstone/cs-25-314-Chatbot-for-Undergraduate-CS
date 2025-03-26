from fastapi import FastAPI, Request
from pydantic import BaseModel
from chat3 import Chatbot
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

chatbot = Chatbot()
templates = Jinja2Templates(directory="templates")  

class ChatRequest(BaseModel):
    message: str

@app.get("/", response_class=HTMLResponse)
async def test_webpage(request: Request):
    return templates.TemplateResponse("test_webpage.html", {"request": request})

@app.post("/chat")
async def chat(request: ChatRequest):
    bot_reply = chatbot.ask_response(request.message)
    return {"reply": bot_reply}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)