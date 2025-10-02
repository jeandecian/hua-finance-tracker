from pypdf import PdfReader
from sys import argv


def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""

    for page in reader.pages:
        text += page.extract_text() + "\n"

    return text


def save_text_to_file(text, file_path):
    with open(file_path, "w") as text_file:
        text_file.write(text)


if __name__ == "__main__":
    pdf_path = argv[1]
    extracted_text = extract_text_from_pdf(pdf_path)
    save_text_to_file(extracted_text, pdf_path.split(".")[0] + ".txt")
