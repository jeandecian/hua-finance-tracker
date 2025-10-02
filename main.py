from pypdf import PdfReader
from sys import argv
import re

CATEGORIES = ("Achat", "Dépôt", "Intérêt", "Ouverture", "Retrait", "Solde", "Virement")


def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""

    for page in reader.pages:
        text += page.extract_text() + "\n"

    return text


def save_text_to_file(text, file_path):
    with open(file_path, "w") as text_file:
        text_file.write(text)


def get_dates_from_text(text):
    dates = re.findall(r"(?:0?[1-9]|[12]\d|3[01])\s[A-Z]{3}", text)

    return dates


def get_descriptions_from_text(text):
    descriptions = []

    for line in text.split("\n"):
        if line.startswith(CATEGORIES):
            for category in CATEGORIES:
                line = line.replace(category, f";{category}")

            descriptions.extend(line.split(";")[1:])

    return descriptions


if __name__ == "__main__":
    pdf_path = argv[1]
    extracted_text = extract_text_from_pdf(pdf_path)
    save_text_to_file(extracted_text, pdf_path.split(".")[0] + ".txt")

    transactions = {
        "Date": get_dates_from_text(extracted_text),
        "Description": get_descriptions_from_text(extracted_text),
    }

    print(transactions)
