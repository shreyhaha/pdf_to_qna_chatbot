import streamlit as st
from pdf_parser import extract_text_from_pdf
from rag_chatbot import create_qa_chain

st.set_page_config(page_title="PDF QnA Chatbot", page_icon="📄")
st.title("📄 Ask Questions From Any PDF")

uploaded_file = st.file_uploader("Upload your PDF file", type="pdf")

if uploaded_file:
    with st.spinner("Extracting text (PyPDF2 or OCR)..."):
        text = extract_text_from_pdf(uploaded_file)
        if not text or text.startswith("OCR failed"):
            st.error("Could not extract text from the PDF.")
        else:
            qa_chain = create_qa_chain(text)
            st.success("Text extracted and indexed! Ask your questions 👇")

            query = st.text_input("Ask a question:")
            if query:
                with st.spinner("Generating answer..."):
                    answer = qa_chain.run(query)
                    st.markdown(f"**Answer:** {answer}")
