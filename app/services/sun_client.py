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
            "status": "pending",
            "message": "SUN generation on the way!🌻"
        }