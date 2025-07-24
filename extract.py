import fitz

def extract_text(path):
    """
    Extracts and returns all text from a PDF file at the given path.
    """
    texts = []
    with fitz.open(path) as doc:
        for page in doc:
            texts.append(page.get_text())
    return "".join(texts).strip()