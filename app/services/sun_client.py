import uuid

from app.core.logger import logger


class SunClient:

    async def generate_audio_course(
        self,
        prompt: str
    ):

        logger.info(
            "Generating SUN audio course..."
        )

        return {
            "job_id": str(uuid.uuid4()),
            "status": "queued",
            "audio_duration": "5 minutes",
            "message": "SUN audio generated! 🌻"
        }