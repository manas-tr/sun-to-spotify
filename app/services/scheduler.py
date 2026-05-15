from apscheduler.schedulers.asyncio import AsyncIOScheduler

from app.core.logger import logger


scheduler = AsyncIOScheduler()


def start_scheduler(job_function):

    scheduler.add_job(
        job_function,
        trigger="cron",
        hour=7,
        minute=0
    )

    scheduler.start()

    logger.info(
        "SUN-flower scheduler started 🌻"
    )