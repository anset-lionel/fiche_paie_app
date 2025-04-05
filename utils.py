# utils.py

import io
import fitz  # PyMuPDF
from pypdf import PdfWriter, PdfReader

def extraire_fiches_par_identifiant(pdf_file, identifiant):
    # On lit le PDF avec PyMuPDF (fitz)
    pdf_bytes = pdf_file.read()
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")

    # Création du writer pour le nouveau PDF
    writer = PdfWriter()

    # Liste pour debug si besoin
    pages_extraites = []

    for i, page in enumerate(doc):
        text = page.get_text()
        if identifiant in text:
            # Si l'identifiant est trouvé, on ajoute cette page au nouveau PDF
            pages_extraites.append(i)
            page_pdf = PdfReader(io.BytesIO(pdf_bytes)).pages[i]
            writer.add_page(page_pdf)

    if pages_extraites:
        output_buffer = io.BytesIO()
        writer.write(output_buffer)
        output_buffer.seek(0)
        return output_buffer
    else:
        return None
