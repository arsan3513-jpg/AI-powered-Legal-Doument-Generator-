import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-1.5-pro")


class GeminiDocumentGenerator:

    @staticmethod
    def generate_document(
        document_type,
        parties,
        terms,
        dates
    ):

        prompt = f"""
You are an AI legal document drafting assistant.

Create a professional {document_type}.

PARTIES:
{parties}

TERMS AND CONDITIONS:
{terms}

EFFECTIVE DATE:
{dates}

Create the document with:

1. Title
2. Introduction
3. Parties
4. Purpose
5. Terms and Conditions
6. Responsibilities
7. Confidentiality
8. Termination
9. Effective Date
10. Signature section

Use clear and formal language.

Do not invent information that was not provided.

Add a note that the generated document
should be reviewed by a qualified legal professional
before being used.

Return only the document.
"""

        response = model.generate_content(prompt)

        return response.text
