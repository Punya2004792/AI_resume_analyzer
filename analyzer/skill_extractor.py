import re


TECHNICAL_KEYWORDS = [
    "python",
    "java",
    "c++",
    "javascript",
    "typescript",

    "flask",
    "django",
    "fastapi",

    "html",
    "css",
    "react",
    "node.js",

    "sql",
    "mysql",
    "postgresql",
    "mongodb",

    "rest api",
    "api",

    "git",
    "github",

    "docker",
    "kubernetes",

    "aws",
    "azure",
    "google cloud",

    "machine learning",
    "deep learning",
    "artificial intelligence",

    "pandas",
    "numpy",
    "scikit-learn",

    "tensorflow",
    "pytorch",

    "data science",
    "data analysis",

    "computer vision",
    "natural language processing",

    "opencv",
    "nlp",

    "fastapi",
    "streamlit"
]


SOFT_SKILLS = [
    "communication",
    "teamwork",
    "leadership",
    "problem solving",
    "problem-solving",
    "critical thinking",
    "time management",
    "adaptability",
    "collaboration",
    "creativity",
    "decision making",
    "decision-making"
]


EDUCATION_KEYWORDS = [
    "bachelor's degree",
    "bachelor degree",
    "bachelor",
    "computer science",
    "information technology",
    "software engineering",
    "computer engineering",
    "information science",
    "engineering degree",
    "master's degree",
    "master degree",
    "diploma"
]


def normalize_text(text):

    if not text:
        return ""

    text = text.lower()
    text = re.sub(r"\s+", " ", text)

    return text.strip()


def extract_keywords(text):

    text = normalize_text(text)

    found = []

    all_keywords = (
        TECHNICAL_KEYWORDS
        + SOFT_SKILLS
        + EDUCATION_KEYWORDS
    )

    for keyword in all_keywords:

        if keyword in text:
            found.append(keyword)

    return sorted(set(found))


def extract_skill_categories(text):

    text = normalize_text(text)

    technical = []
    soft = []
    education = []

    for keyword in TECHNICAL_KEYWORDS:

        if keyword in text:
            technical.append(keyword)

    for keyword in SOFT_SKILLS:

        if keyword in text:
            soft.append(keyword)

    for keyword in EDUCATION_KEYWORDS:

        if keyword in text:
            education.append(keyword)

    return {
        "technical": sorted(set(technical)),
        "soft": sorted(set(soft)),
        "education": sorted(set(education))
    }


def analyze_keywords(resume_text, job_description):

    resume_keywords = set(
        extract_keywords(resume_text)
    )

    job_keywords = set(
        extract_keywords(job_description)
    )

    matched_keywords = sorted(
        resume_keywords & job_keywords
    )

    missing_keywords = sorted(
        job_keywords - resume_keywords
    )

    if job_keywords:

        coverage = (
            len(matched_keywords)
            / len(job_keywords)
        ) * 100

    else:

        coverage = 0

    return {

        "resume_keywords":
            sorted(resume_keywords),

        "job_keywords":
            sorted(job_keywords),

        "matched_keywords":
            matched_keywords,

        "missing_keywords":
            missing_keywords,

        "coverage":
            round(coverage, 2)
    }