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

from app.utils.storage import daily_brief

from contextlib import asynccontextmanager

from app.services.scheduler import start_scheduler

@asynccontextmanager
async def lifespan(app: FastAPI):

    start_scheduler(run_daily_pipeline)

    yield


app = FastAPI(
    lifespan=lifespan,
    title="SUN-flower",
    description="Your daily SUN-rise, delivered before your commute.",
    version="0.1.0"
)

async def run_daily_pipeline():

    logger.info(
        "Running daily SUN-rise pipeline"
    )

    topics = await fetch_topics()

    deduplicated_topics = deduplicate_topics(
        topics
    )

    interests = load_interests()

    ranked_topics = rank_interest(
        deduplicated_topics,
        interests
    )

    top_topics = ranked_topics[:3]

    sun_client = SunClient()

    prompts = []

    for topic in top_topics:

        prompt = build_prompt(topic)

        sun_job = await sun_client.generate_audio_course(
            prompt
        )

        sun_result = await sun_client.poll_generation_status(
            sun_job["job_id"]
        )

        prompts.append({
            "topic": topic.title,
            "prompt": prompt,
            "sun_job": sun_job,
            "sun_result": sun_result
        })

    saved_file = daily_brief(prompts)

    logger.info(
        f"Daily SUN-rise saved to {saved_file}"
    )

    return prompts


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

        sun_job = await sun_client.generate_audio_course(
            prompt
        )

        sun_result = await sun_client.poll_generation_status(
            sun_job["job_id"]
        )

        prompts.append({
            "topic": topic.title,
            "prompt": prompt,
            "sun_job": sun_job,
            "sun_result": sun_result
        })

    logger.info(
        f"Generated {len(prompts)} personalized prompts"
    )

    saved_file = daily_brief(prompts)

    logger.info(
        f"Saved daily brief to {saved_file}"
    )

    return {
        "interests": interests,
        "total_topics": len(top_topics),
        "saved_file": saved_file,
        "daily_brief": prompts
    }