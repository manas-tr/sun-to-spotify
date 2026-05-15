from app.models.topic import Topic

def generate_context(topic: Topic) -> str:

    if topic.summary.strip():
        return topic.summary

    return (
        f"This topic is currently trending in {topic.source}. "
        f"It focuses on: {topic.title}."
    )


def build_prompt(topic: Topic) -> str:

    context = generate_context(topic)

    prompt = f"""
Create a sharp 5-minute audio learning brief.

Topic:
{topic.title}

Context:
{context}

The brief should:
- explain what happened
- explain why it matters today
- explain the broader implications
- stay concise and conversational
- sound like a smart friend explaining something important
- avoid hype and filler

Structure:
1. What happened
2. Why people care
3. What changes next
4. Key takeaway

End with:
"Here's what to watch next."

Source:
{topic.source}
"""

    return prompt.strip()