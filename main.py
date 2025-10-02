from pypdf import PdfReader
from sys import argv


def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""

    for page in reader.pages:
        text += page.extract_text() + "\n"

    return text


if __name__ == "__main__":
    pdf_path = argv[1]
    extracted_text = extract_text_from_pdf(pdf_path)
    print(extracted_text)
