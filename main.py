from fastapi import FastAPI, Query
from starlette.responses import RedirectResponse, HTMLResponse
from core.wayback_parser import parse, retrieve_url
from uuid import uuid4

app = FastAPI()

content_store = {}


@app.get("/process-url/")
async def process_url(url: str = Query(None)):
    if not url:
        return "URL parameter is missing"
    target_url = retrieve_url(url)
    page = parse(target_url)

    page_id = str(uuid4())

    content_store[page_id] = page

    return RedirectResponse(url=f"/display?content_id={page_id}")


@app.get("/display")
async def display(content_id: str = Query(None)):
    if not content_id or content_id not in content_store:
        return "Invalid or missing content ID"

    processed_content = content_store[content_id]
    return HTMLResponse(content=processed_content)