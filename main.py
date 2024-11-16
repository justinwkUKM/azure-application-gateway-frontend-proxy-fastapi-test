from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import requests




app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST","OPTIONS"],
    allow_headers=["*"],
)

class Message(BaseModel):
    message: str


@app.post("/proxy")
def proxy_request(url: str):
    """
    Makes a GET request to the provided URL and returns the response.
    """
    try:
        response = requests.get(url)
        return {
            "status_code": response.status_code,
            "body": response.text
        }
    except Exception as e:
        return {"error": str(e)}
    
@app.get('/')
async def root():
    return {"message": "Welcome to Frontend Proxy Test Server"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)