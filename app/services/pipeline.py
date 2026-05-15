from app.core.logger import logger

from app.ml.ranker import (
    deduplicate_topics,
    rank_interest
)

from app.services.fetcher import fetch_topics
from app.services.prompt_builder import build_prompt
from app.services.sun_client import SunClient

from app.utils.helper import load_interests
from app.utils.storage import daily_brief


async def run_pipeline():

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
            "audio_status": sun_result["status"],
            "audio_url": sun_result["audio_url"],
            "summary": (
                f"A personalized SUN brief about "
                f"{topic.title}"
            )
        })

    saved_file = daily_brief(prompts)

    logger.info(
        f"Saved daily brief to {saved_file}"
    )

    return {
        "interests": interests,
        "total_topics": len(top_topics),
        "saved_file": saved_file,
        "sunrise_brief": prompts
    }