import os
import PyPDF2

def extract_text_from_file(file_path: str) -> str:
    """
    Extrai texto de arquivos .txt ou .pdf.
    """
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"Arquivo não encontrado: {file_path}")

    if file_path.lower().endswith(".txt"):
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()

    elif file_path.lower().endswith(".pdf"):
        text = ""
        with open(file_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                text += page.extract_text() or ""
        return text

    else:
        raise ValueError("Formato de arquivo não suportado. Use .txt ou .pdf")
