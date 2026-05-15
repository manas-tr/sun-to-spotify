from fastapi import FastAPI
from app.ml.ranker import deduplicate_topics

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

    deduplicated_topics = deduplicate_topics(topics)

    return {
        "original_count": len(topics),
        "final_count": len(deduplicated_topics),
        "topics": deduplicated_topics
    }