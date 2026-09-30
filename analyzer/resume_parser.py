import re
from pypdf import PdfReader


def clean_resume_text(text):
    """
    Cleans extracted PDF text while preserving meaningful content.
    """

    if not text:
        return ""

    text = text.replace("\x00", " ")

    # Fix excessive spaces
    text = re.sub(r"[ \t]+", " ", text)

    # Fix common character-by-character PDF extraction
    text = re.sub(
        r"(?<!\w)"
        r"([A-Za-z])"
        r"(?:\s+([A-Za-z])){2,}"
        r"(?!\w)",
        lambda match: match.group(0).replace(" ", ""),
        text
    )

    # Reduce excessive blank lines
    text = re.sub(r"\n\s*\n+", "\n\n", text)

    return text.strip()


def extract_text_from_pdf(file_path):
    """
    Extract text from all pages of a PDF.
    """

    reader = PdfReader(file_path)

    extracted_text = []

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            extracted_text.append(page_text)

    combined_text = "\n".join(extracted_text)

    return clean_resume_text(combined_text)