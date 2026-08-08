from app.extractor import extract_text_from_pdf
from fastapi import FastAPI, File, HTTPException, UploadFile

app = FastAPI(title="ProyectoIA PDF Extractor", version="1.0.0")


@app.get("/health")
def health():
    return {"success": True, "message": "PDF Extractor funcionando correctamente"}


@app.post("/extract")
async def extract_pdf(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="El archivo debe ser un PDF.")

    pdf_bytes = await file.read()

    result = extract_text_from_pdf(pdf_bytes)

    return {"success": True, **result}
