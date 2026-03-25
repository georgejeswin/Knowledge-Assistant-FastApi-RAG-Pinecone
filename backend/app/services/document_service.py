import os
from app.utils.file_parser import extract_text_from_pdf
from app.repositories.document_repository import DocumentRepository
from app.workers.tasks import process_document

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


class DocumentService:

    @staticmethod
    async def upload_document(db, file, user):
        file_path = f"{UPLOAD_DIR}/{file.filename}"

        with open(file_path, "wb") as f:
            content = await file.read()
            f.write(content)

        extracted_text = extract_text_from_pdf(file_path)

        doc = await DocumentRepository.create(
            db,
            filename=file.filename,
            content=extracted_text,
            owner_id=user.id
        )

        #  Background processing
        process_document.delay(doc.id)

        return doc