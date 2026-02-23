from Modules1.summarizer import generate_summary

sample_text = """
SqueezeReads is an innovative AI-powered application that allows users to upload long documents
and generate chapter-wise abstractive summaries. With features like audio playback, multiple 
summary lengths, and download options, it's the perfect tool for students, researchers, and readers.
"""

print("Short Summary:\n", generate_summary(sample_text, "short"))
