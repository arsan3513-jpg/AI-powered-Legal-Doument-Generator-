import streamlit as st
import requests

from utils.docx_generator import format_docx
from utils.pdf_generator import format_pdf


API_URL = "http://127.0.0.1:8000/generate"


st.set_page_config(
    page_title="LegalEase",
    page_icon="⚖️",
    layout="wide"
)


st.title("⚖️ LegalEase")

st.write(
    "AI-Powered Legal Document Generator"
)


# -----------------------------
# INPUT SECTION
# -----------------------------

document_type = st.selectbox(
    "Select Document Type",
    [
        "Employment Contract",
        "Non-Disclosure Agreement",
        "Lease Agreement",
        "Service Agreement",
        "Freelance Contract",
        "General Agreement"
    ]
)


parties = st.text_area(
    "Parties Involved",
    placeholder=(
        "Example: "
        "John Doe (Employee), "
        "ABC Company (Employer)"
    )
)


terms = st.text_area(
    "Terms & Conditions",
    placeholder=(
        "Enter terms separated by semicolon ;"
    )
)


dates = st.text_input(
    "Effective Date",
    placeholder="Example: 10/10/2026"
)


# -----------------------------
# GENERATE
# -----------------------------

if st.button(
    "Generate Document",
    type="primary"
):

    if not parties or not terms or not dates:

        st.warning(
            "Please fill all required fields."
        )

    else:

        data = {

            "document_type": document_type,

            "parties": parties,

            "terms": terms,

            "dates": dates
        }

        try:

            response = requests.post(
                API_URL,
                json=data
            )

            result = response.json()

            if result["success"]:

                st.session_state["document"] = (
                    result["document"]
                )

                st.success(
                    "Document generated successfully!"
                )

        except Exception as e:

            st.error(
                f"Backend connection error: {e}"
            )


# -----------------------------
# PREVIEW & EDIT
# -----------------------------

if "document" in st.session_state:

    st.subheader("📄 Generated Document")

    edited_document = st.text_area(
        "Edit Document",
        value=st.session_state["document"],
        height=500
    )

    st.session_state["document"] = edited_document


    # -------------------------
    # DOWNLOAD TXT
    # -------------------------

    st.download_button(
        label="⬇️ Download TXT",
        data=edited_document,
        file_name="LegalEase_Document.txt",
        mime="text/plain"
    )


    # -------------------------
    # DOWNLOAD DOCX
    # -------------------------

    docx_file = format_docx(
        edited_document,
        document_type
    )

    docx_path = "LegalEase_Document.docx"

    docx_file.save(docx_path)

    with open(docx_path, "rb") as file:

        st.download_button(
            label="⬇️ Download DOCX",
            data=file,
            file_name="LegalEase_Document.docx",
            mime=(
                "application/"
                "vnd.openxmlformats-officedocument"
                ".wordprocessingml.document"
            )
        )


    # -------------------------
    # DOWNLOAD PDF
    # -------------------------

    pdf_file = format_pdf(
        edited_document,
        document_type
    )

    pdf_bytes = pdf_file.output(
        dest="S"
    ).encode("latin-1")


    st.download_button(
        label="⬇️ Download PDF",
        data=pdf_bytes,
        file_name="LegalEase_Document.pdf",
        mime="application/pdf"
            )
