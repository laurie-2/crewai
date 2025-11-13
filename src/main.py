from fastapi import FastAPI

app = FastAPI(title="CrewAI")

@app.get("/")
async def home():
    return {"message": "CrewAI running successfully"}

@app.get("/health")
async def health():
    return {"status": "ok"}

from fastapi import Response

@app.get("/favicon.ico")
async def favicon():
    return Response(status_code=204)  # No Content
