import asyncio
import uuid

from app.core.logger import logger


class SunClient:

    async def generate_audio_course(
        self,
        prompt: str
    ):

        job_id = str(uuid.uuid4())

        logger.info(
            f"Created SUN job: {job_id}"
        )

        return {
            "job_id": job_id,
            "status": "queued"
        }

    async def poll_generation_status(
        self,
        job_id: str
    ):

        logger.info(
            f"Polling SUN job: {job_id}"
        )

        await asyncio.sleep(2)

        return {
            "job_id": job_id,
            "status": "SUN audio generated! 🌻",
            "audio_url": (
                f"https://audio.sunflower.ai/{job_id}.mp3"
            )
        }