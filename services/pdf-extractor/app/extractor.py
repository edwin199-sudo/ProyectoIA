import fitz


def extract_text_from_pdf(pdf_bytes: bytes):
    document = fitz.open(stream=pdf_bytes, filetype="pdf")

    # Guardar el número de páginas antes de cerrar el documento
    pages = len(document)

    text = ""

    for page in document:
        text += page.get_text()

    characters = len(text)

    document.close()

    return {
        "pages": pages,
        "characters": characters,
        "text": text
    }