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
    
@app.post("/proxy_two_urls")
def proxy_request2(first_url: str, second_url: str):
    """
    1. Makes a GET request to the first_url
    2. Takes that response and sends it as a body parameter in a POST request to second_url
    """
    try:
        print(first_url)
        print(second_url)
        # Second POST request using first response as body
        response = requests.post(first_url, params={"url": second_url})
        print(response.status_code)
        data = response.json()
        
        
        return {
            
                "status_code": response.status_code,
                "body": data["result"]
            
        }
    except Exception as e:
        return {"error": str(e)}
    
@app.get('/')
async def root():
    return {"message": "Welcome to Frontend Proxy Test Server"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)