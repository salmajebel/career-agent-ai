import streamlit as st
from agent import career_agent

st.set_page_config(page_title="CareerAgent", layout="wide")

st.title("🧠 CareerAgent - AI Career Assistant")

# INPUT CV
cv = st.text_area("Paste your CV here")

if st.button("Analyze CV"):

    with st.spinner("Analyzing with AI..."):
        result = career_agent(cv)

    st.success("Analysis complete!")

    st.subheader("📄 AI Result")
    st.write(result)

    st.download_button(
        "⬇ Download Report",
        result,
        file_name="career_report.txt"
    )
