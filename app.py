# app.py

import streamlit as st
import torch


from Modules1.file_handler import read_file
from Modules1.summarizer import generate_summary
from Modules1.chapter_splitter import split_into_chapters
from Modules1.text_reader import speak_text
from Modules1.file_handler import save_summary_as_txt, save_summary_as_pdf

st.set_page_config(page_title="📚 SqueezeReads", layout="wide")

st.title("📘 SqueezeReads")
st.markdown("Summarize your chapters smartly with AI 💡")

uploaded_file = st.file_uploader("Upload a PDF, DOCX or TXT file", type=["pdf", "docx", "txt"])

if uploaded_file:
    # Extract raw text from file
    with st.spinner("Reading file..."):
        full_text = read_file(uploaded_file)

    # Chapter splitting
    chapters = split_into_chapters(full_text)

    # User selects summary length
    summary_len = st.radio("Choose summary length:", ["short", "medium", "long"], horizontal=True)

    # Iterate through chapters
    for i, (title, content) in enumerate(chapters):
        st.subheader(f"📖 {title}")

        if st.button(f"Summarize Chapter {i+1}", key=f"sum_{i}"):
            with st.spinner("Summarizing..."):
                summary = generate_summary(content, summary_len)
                st.success("✅ Summary Ready!")
                st.write(summary)

                # Download summary
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.download_button("⬇️ Download TXT", save_summary_as_txt(summary), f"{title}.txt")
                with col2:
                    st.download_button("📄 Download PDF", save_summary_as_pdf(summary), f"{title}.pdf")
                with col3:
                    if st.button("🔊 Read Aloud", key=f"audio_{i}"):
                        speak_text(summary)
