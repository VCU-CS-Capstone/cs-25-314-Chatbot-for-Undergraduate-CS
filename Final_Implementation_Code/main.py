from fastapi import FastAPI, Request, WebSocket, WebSocketDisconnect
from pydantic import BaseModel
from chat3 import Chatbot
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

chatbot = Chatbot()
active_connections = set()
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

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):

    await websocket.accept()
    active_connections.add(websocket)

    print(f"New connection: {websocket.client}")


    try:
        while True:
            data = await websocket.receive_text()
            bot_reply = chatbot.ask_response(data)
            await websocket.send_text(bot_reply)
    except WebSocketDisconnect:
        print(f"Disconnected: {websocket.client}")
        active_connections.remove(websocket)
    except Exception as e:
        print(f"Error: {e}")
        active_connections.remove(websocket)



if __name__ == "__main__":
    
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

