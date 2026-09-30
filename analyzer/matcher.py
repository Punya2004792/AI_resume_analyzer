from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from .skill_extractor import extract_keywords


def calculate_similarity(
    resume_text,
    job_description
):

    documents = [
        resume_text,
        job_description
    ]

    try:

        vectorizer = TfidfVectorizer(
            stop_words="english"
        )

        matrix = vectorizer.fit_transform(
            documents
        )

        similarity = cosine_similarity(
            matrix[0:1],
            matrix[1:2]
        )[0][0]

        return round(
            similarity * 100,
            2
        )

    except ValueError:

        return 0


def calculate_skill_match(
    resume_text,
    job_description
):

    resume_keywords = set(
        extract_keywords(resume_text)
    )

    job_keywords = set(
        extract_keywords(job_description)
    )

    matched = sorted(
        resume_keywords & job_keywords
    )

    missing = sorted(
        job_keywords - resume_keywords
    )

    if job_keywords:

        score = (
            len(matched)
            / len(job_keywords)
        ) * 100

    else:

        score = 0

    return {

        "score":
            round(score, 2),

        "matched":
            matched,

        "missing":
            missing
    }


def calculate_final_score(
    skill_score,
    similarity_score,
    keyword_coverage
):

    score = (
        (skill_score * 0.45)
        + (similarity_score * 0.30)
        + (keyword_coverage * 0.25)
    )

    return round(score, 2)