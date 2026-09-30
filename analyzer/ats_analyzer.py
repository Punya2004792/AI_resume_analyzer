def analyze_ats(resume_text):

    text = resume_text.lower()

    sections = {

        "Contact Information": [
            "email",
            "@",
            "phone",
            "mobile",
            "contact"
        ],

        "Education": [
            "education",
            "academic",
            "degree",
            "university",
            "college"
        ],

        "Experience": [
            "experience",
            "work experience",
            "employment",
            "internship"
        ],

        "Projects": [
            "projects",
            "project"
        ],

        "Skills": [
            "skills",
            "technical skills",
            "technologies"
        ],

        "Certifications": [
            "certification",
            "certifications",
            "certificate"
        ]
    }

    detected = []
    missing = []

    for section, keywords in sections.items():

        found = any(
            keyword in text
            for keyword in keywords
        )

        if found:

            detected.append(section)

        else:

            missing.append(section)

    score = (
        len(detected)
        / len(sections)
    ) * 100

    return {

        "score":
            round(score, 2),

        "detected":
            detected,

        "missing":
            missing
    }