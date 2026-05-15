from fastapi import FastAPI

from app.services.fetcher import fetch_topics

app = FastAPI(
    title="SUN-flower",
    description="Your daily SUN-rise, delivered before your commute.",
    version="0.1.0"
)


@app.get("/")
async def root():
    return {
        "message": "SUN-flower has bloomed! 🌻"
    }


@app.get("/topics")
async def get_topics():
    topics = await fetch_topics()

    return {
        "count": len(topics),
        "topics": topics
    }