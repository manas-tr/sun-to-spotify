from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.logger import logger

from app.ml.ranker import deduplicate_topics

from app.services.fetcher import fetch_topics
from app.services.pipeline import run_pipeline
from app.services.scheduler import start_scheduler


@asynccontextmanager
async def lifespan(app: FastAPI):

    start_scheduler(run_pipeline)

    yield


app = FastAPI(
    lifespan=lifespan,
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

    deduplicated_topics = deduplicate_topics(
        topics
    )

    return {
        "original_count": len(topics),
        "final_count": len(deduplicated_topics),
        "topics": deduplicated_topics
    }


@app.get("/prompt")
async def generate_prompt():

    logger.info(
        "Starting personalized brief generation"
    )

    result = await run_pipeline()

    logger.info(
        "Pipeline execution complete"
    )

    return result