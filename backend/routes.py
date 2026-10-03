from fastapi import APIRouter

from backend.models import DocumentRequest
from backend.ai_core.gemini_generator import (
    GeminiDocumentGenerator
)

router = APIRouter()


@router.post("/generate")
def generate_document(request: DocumentRequest):

    document = GeminiDocumentGenerator.generate_document(
        request.document_type,
        request.parties,
        request.terms,
        request.dates
    )

    return {
        "success": True,
        "document": document
    }
