from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from app.models.topic import Topic
from app.core.logger import logger

import numpy as np


SIMILARITY_THRESHOLD = 0.57

def deduplicate_topics(topics: list[Topic]) -> list[Topic]:

    if not topics:
        return []

    logger.info("Running topic deduplication..")

    texts = [
        f"{topic.title} {topic.summary}"
        for topic in topics
    ]

    vectorizer = TfidfVectorizer(stop_words="english")

    tfidf_matrix = vectorizer.fit_transform(texts)

    similarity_matrix = cosine_similarity(tfidf_matrix)

    selected_topics = []
    skipped_indices = set()

    for i in range(len(topics)):
        if i in skipped_indices:
            continue

        selected_topics.append(topics[i])

        for j in range(i + 1, len(topics)):
            similarity_score = similarity_matrix[i][j]

            if similarity_score > SIMILARITY_THRESHOLD:
                skipped_indices.add(j)

    logger.info(
        f"Deduplicated {len(topics)} topics into {len(selected_topics)}"
    )

    return selected_topics

def rank_interest(
    topics: list[Topic],
    interests: list[str]
) -> list[Topic]:


    if not topics:
        return []

    logger.info("Ranking topics..")

    topic_texts = [
        f"{topic.title} {topic.summary}"
        for topic in topics
    ]

    combined_texts = interests + topic_texts

    vectorizer = TfidfVectorizer(stop_words="english")

    tfidf_matrix = vectorizer.fit_transform(combined_texts)

    interest_vectors = tfidf_matrix[:len(interests)]

    topic_vectors = tfidf_matrix[len(interests):]

    scores = []

    for idx, topic_vector in enumerate(topic_vectors):
        similarities = cosine_similarity(
            topic_vector,
            interest_vectors
        )

        avg_score = np.mean(similarities)

        scores.append((avg_score, topics[idx]))

    ranked_topics = [
        topic
        for _, topic in sorted(scores, key=lambda x: x[0], reverse=True)
    ]

    logger.info("Topic ranking done!")

    return ranked_topics