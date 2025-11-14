from fastapi import FastAPI, Response
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

app = FastAPI(title="CrewAI")

# Serve static files (manifest.json, icons, etc.)
app.mount("/static", StaticFiles(directory="src/static"), name="static")

# Root route serves HTML so manifest works
@app.get("/", response_class=HTMLResponse)
async def home():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>CrewAI</title>
        <link rel="manifest" href="/static/manifest.json">
    </head>
    <body>
        <h1>Welcome to CrewAI</h1>
        <p>Your app is running!</p>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)

# Health check route
@app.get("/health")
async def health():
    return {"status": "ok"}

# Favicon route (prevents 404)
@app.get("/favicon.ico")
async def favicon():
    return Response(status_code=204)  # No Content
