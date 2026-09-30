def generate_recommendations(
    final_score,
    matched_skills,
    missing_skills,
    ats_missing,
    keyword_coverage
):

    recommendations = []


    if missing_skills:

        recommendations.append(
            "Consider strengthening your resume with "
            "relevant skills such as "
            + ", ".join(missing_skills[:5])
            + "."
        )


    if keyword_coverage < 60:

        recommendations.append(
            "Your keyword coverage is relatively low. "
            "Consider naturally including important "
            "job-related terminology in relevant "
            "projects and experience sections."
        )


    if ats_missing:

        recommendations.append(
            "Consider adding clearly labelled sections "
            "for: "
            + ", ".join(ats_missing)
            + "."
        )


    if final_score >= 75:

        recommendations.append(
            "Your resume shows strong alignment with "
            "the supplied job description. Consider "
            "adding measurable achievements."
        )

    elif final_score >= 50:

        recommendations.append(
            "Your resume has moderate alignment with "
            "the supplied job description. Tailoring "
            "your projects and technical skills could "
            "improve relevance."
        )

    else:

        recommendations.append(
            "Consider tailoring your resume more closely "
            "to the requirements and terminology used "
            "in the supplied job description."
        )


    return recommendations