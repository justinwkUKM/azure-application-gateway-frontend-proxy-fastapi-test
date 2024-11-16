from fastapi import FastAPI

from typing import Optional, Dict, Any
import uvicorn

app = FastAPI(title="Endpoint Proxy", description="A simple proxy service to make GET requests")

# class EndpointRequest(BaseModel):
#     url: HttpUrl
#     headers: Optional[Dict[str, str]] = None

# class EndpointResponse(BaseModel):
#     status_code: int
#     headers: Dict[str, str]
#     body: Any

# @app.post("/proxy", response_model=EndpointResponse)
# async def proxy_request(request: EndpointRequest):
#     """
#     Makes a GET request to the provided URL and returns the response.
#     """
#     try:
#         async with httpx.AsyncClient() as client:
#             response = await client.get(
#                 str(request.url),
#                 headers=request.headers,
#                 timeout=30.0
#             )
            
#             # Convert headers to dict of strings
#             headers_dict = dict(response.headers)
#             headers_str = {k: str(v) for k, v in headers_dict.items()}
            
#             return EndpointResponse(
#                 status_code=response.status_code,
#                 headers=headers_str,
#                 body=response.text
#             )
            
#     except httpx.TimeoutException:
#         raise HTTPException(status_code=504, detail="Request timed out")
#     except httpx.RequestError as e:
#         raise HTTPException(status_code=400, detail=str(e))

@app.get('/')
async def root():
    return {"message": "Welcome to Frontend Proxy Server"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)