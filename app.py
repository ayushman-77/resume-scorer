import streamlit as st
from extract import extract_text
from score import (
    readability, grammar,
    sections, keywords
)

st.set_page_config(page_title="Resume Scorer", layout="centered")

st.title("📄 AI Resume Scorer")
st.write("Upload your resume (PDF) and get a breakdown of how job-ready and professional it is.")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type="pdf")

if uploaded_file:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    text = extract_text("temp.pdf")

    with st.spinner("Analyzing your resume..."):
        readability_score = readability(text)
        grammar_score = grammar(text)
        sections_score = sections(text)
        keywords_score = keywords(text)

        total = readability_score + grammar_score + sections_score + keywords_score

    st.subheader("🧾 Results")
    st.markdown(f"**📘 Readability Score:** {readability_score}/20")
    st.markdown(f"**🧠 Grammar Score:** {grammar_score}/20")
    st.markdown(f"**📌 Section Score:** {sections_score}/20")
    st.markdown(f"**🔑 Keywords Score:** {keywords_score}/20")
    st.markdown(f"### 🎯 Final Score: `{round(total, 2)}/80`")

    st.markdown("---")
    st.subheader("🛠 Suggestions")

    if "github" not in text.lower():
        st.warning("Consider adding a link to your GitHub or portfolio.")
    if total < 60:
        st.info("Try improving your section structure and including more relevant keywords.")
    if grammar_score < 15:
        st.info("Improve grammar and sentence clarity for a more professional tone.")
