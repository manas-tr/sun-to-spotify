from app.core.logger import logger


class SpotifyClient:

    async def upload_episode(
        self,
        topic: str,
        audio_url: str
    ):

        logger.info(
            f"Uploading '{topic}' to Spotify.."
        )

        return {
            "spotify_status": "uploaded",
            "spotify_episode": (
                f"{topic} | Daily SUN-rise 🌻"
            )
        }