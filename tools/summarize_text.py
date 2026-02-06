def summarize_text(text: str, max_words: int = 5):
    words = text.split()
    return " ".join(words[:max_words])
