# # modules/summarizer.py

# from transformers import pipeline

# # Load the summarization pipeline only once
# summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

# def generate_summary(text: str, length: str = "medium") -> str:
#     """
#     Generate an abstractive summary based on selected length.
    
#     Parameters:
#     - text (str): Input text to summarize
#     - length (str): One of 'short', 'medium', 'long'

#     Returns:
#     - str: Summarized text
#     """
#     if not text.strip():
#         return "⚠️ Empty input provided."

#     max_len_map = {
#         "short": 60,
#         "medium": 120,
#         "long": 200
#     }

#     max_len = max_len_map.get(length, 120)

#     # transformers models can’t handle very long texts in one go
#     if len(text.split()) > 900:
#         text = " ".join(text.split()[:900])  # trim to fit model limits

#     summary_output = summarizer(text, max_length=max_len, min_length=30, do_sample=False)
#     return summary_output[0]['summary_text']

# modules/summarizer.py

from transformers import pipeline

summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

# def chunk_text(text, max_chunk_words=450):
#     words = text.split()
#     return [" ".join(words[i:i + max_chunk_words]) for i in range(0, len(words), max_chunk_words)]

import re

def chunk_text(text, max_chunk_words=450):
    sentences = re.split(r'(?<=[.!?])\s+', text)
    chunks, current_chunk = [], []

    current_len = 0
    for sentence in sentences:
        word_count = len(sentence.split())
        if current_len + word_count <= max_chunk_words:
            current_chunk.append(sentence)
            current_len += word_count
        else:
            chunks.append(" ".join(current_chunk))
            current_chunk = [sentence]
            current_len = word_count
    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks

def generate_summary(text: str, length: str = "medium") -> str:
    if not text.strip():
        return "⚠️ Empty input provided."

    length_map = {
        "short": 60,
        "medium": 120,
        "long": 200
    }
    max_len = length_map.get(length, 120)

    chunks = chunk_text(text)

    full_summary = ""
    for chunk in chunks:
        try:
            summary = summarizer(chunk, max_length=max_len, min_length=30, do_sample=False)
            full_summary += summary[0]['summary_text'].strip() + "\n\n"
        except Exception as e:
            full_summary += f"⚠️ Chunk summarization failed: {e}\n\n"

    return full_summary.strip()
