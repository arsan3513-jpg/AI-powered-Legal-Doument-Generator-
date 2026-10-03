def sanitize_text(text):

    replacements = {
        "“": '"',
        "”": '"',
        "‘": "'",
        "’": "'",
        "–": "-",
        "—": "-"
    }

    for old, new in replacements.items():
        text = text.replace(old, new)

    return text.strip()
