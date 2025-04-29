from fastapi import FastAPI
from pydantic import BaseModel
from router import route_message
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Add CORS settings here
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define the shape of incoming chat requests
class ChatRequest(BaseModel):
    user_id: str = "default"
    message: str

# Define the API endpoint
@app.post("/chat")
def chat(request: ChatRequest):
    user_message = request.message
    user_id = request.user_id
    response = route_message(user_message, user_id)
    return {"response": response}