from fastapi import FastAPI
from app.ml.ranker import deduplicate_topics

from app.services.fetcher import fetch_topics

from app.services.prompt_builder import build_prompt

from app.utils.helper import load_interests
from app.ml.ranker import (
    deduplicate_topics,
    rank_interest
)

from app.core.logger import logger

from app.services.sun_client import SunClient

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

    logger.info("Starting personalized brief generation")

    topics = await fetch_topics()

    deduplicated_topics = deduplicate_topics(topics)

    interests = load_interests()

    ranked_topics = rank_interest(
        deduplicated_topics,
        interests
    )

    top_topics = ranked_topics[:3]

    prompts = []

    sun_client=SunClient()

    for topic in top_topics:

        prompt = build_prompt(topic)

        sun_response = await sun_client.generate_audio_course(prompt)

        prompts.append({
            "topic": topic.title,
            "prompt": prompt,
            "sun_status": sun_response
        })

    logger.info(
        f"Generated {len(prompts)} personalized prompts"
    )

    return {
        "interests": interests,
        "total_topics": len(top_topics),
        "daily_brief": prompts
    }