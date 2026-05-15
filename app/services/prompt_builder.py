from app.models.topic import Topic


def build_prompt(topic: Topic) -> str:

    prompt = f"""
Create a sharp 5-minute audio learning brief.

Topic:
{topic.title}

Context:
{topic.summary}

The brief should:
- explain what happened
- explain why it matters today
- explain what changes because of it
- stay concise and conversational
- sound like an intelligent friend teaching another curious person
- avoid hype and filler

End with:
"Here's what to watch next."

Source:
{topic.source}
"""

    return prompt.strip()