from fastapi import FastAPI
from app.ml.ranker import deduplicate_topics

from app.services.fetcher import fetch_topics

from app.services.prompt_builder import build_prompt


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

@app.get("/prompt")
async def generate_prompt():
    topics = await fetch_topics()

    deduplicated_topics = deduplicate_topics(topics)

    if not deduplicated_topics:
        return {
            "error": "No topics available"
        }

    topic = deduplicated_topics[0]

    prompt = build_prompt(topic)

    return {
        "topic": topic.title,
        "prompt": prompt
    } 