# modules/chapter_splitter.py

import re

def split_into_chapters(text):
    """
    Splits the text into chapters based on common patterns like 'Chapter 1', 'CHAPTER I', etc.
    Returns a list of (title, content) tuples.
    """
    pattern = r'(Chapter\s+\d+|CHAPTER\s+\w+|CHAPTER\s+\d+|CHAPTER\s+[IVXLC]+)'
    matches = list(re.finditer(pattern, text))

    if not matches:
        return [("Full Text", text)]

    chapters = []
    for i in range(len(matches)):
        start = matches[i].start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        title = matches[i].group().strip()
        content = text[start:end].strip()
        chapters.append((title, content))

    return chapters
