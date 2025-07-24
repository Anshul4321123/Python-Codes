from fastapi import FastAPI, Request
import time

app = FastAPI()

@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    
    response = await call_next(request)
    
    duration = time.time() - start_time
    log_details = f"{request.method} {request.url.path} completed in {duration:.4f}s"
    
    print(log_details)
    return response

@app.get("/")
def read_root():
    return {"message": "Hello, world"}
