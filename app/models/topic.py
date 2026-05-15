from pydantic import BaseModel


class Topic(BaseModel):
    title: str
    summary: str
    source: str
    url: str
    timestamp: str