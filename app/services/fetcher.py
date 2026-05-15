import feedparser

from app.models.topic import Topic
from app.core.logger import logger

from app.utils.helper import clean_html


RSS_FEEDS = [
    "https://hnrss.org/frontpage",
    "https://feeds.feedburner.com/TechCrunch/",
]


async def fetch_topics() -> list[Topic]:
    topics = []

    logger.info("Fetching topics..")

    for feed_url in RSS_FEEDS:
        feed = feedparser.parse(feed_url)

        for entry in feed.entries[:5]:
            topic = Topic(
                title=entry.get("title", ""),
                summary=clean_html(entry.get("summary", "")),
                source=feed.feed.get("title", "Unknown"),
                url=entry.get("link", ""),
                timestamp=entry.get("published", "")
            )

            topics.append(topic)

    logger.info(f"Fetched {len(topics)} topics")

    return topics