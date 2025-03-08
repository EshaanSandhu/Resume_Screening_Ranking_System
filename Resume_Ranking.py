import streamlit as st
from PyPDF2 import PdfReader
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt
from collections import Counter
import re

# Ensure that st.set_page_config() is the FIRST Streamlit command
st.set_page_config(layout="wide")

# Function to extract text from PDF
def extract_text_from_pdf(file):
    pdf = PdfReader(file)
    text = ""
    for page in pdf.pages:
        text += page.extract_text()
    return text

# Function to rank resumes based on job description
def rank_resumes(job_description, resumes):
    documents = [job_description] + resumes
    vectorizer = TfidfVectorizer().fit_transform(documents)
    vectors = vectorizer.toarray()
    job_description_vector = vectors[0]
    resume_vectors = vectors[1:]
    cosine_similarities = cosine_similarity([job_description_vector], resume_vectors).flatten()
    return cosine_similarities

# Function to extract major skills
def extract_major_skills(resumes):
    all_skills = []
    for resume in resumes:
        skills = [skill.lower() for skill in ["python", "java", "sql", "data analysis", "machine learning", "communication", "project management", "javascript", "c++"] if skill.lower() in resume.lower()]
        all_skills.extend(skills)
    return all_skills

# Streamlit app
st.title("AI Resume Screening & Candidate Ranking System")

col1, col2 = st.columns([1, 2])

with col1:
    st.header("Job Description")
    job_description = st.text_area("Enter the job description", height=150)

    st.header("Upload Resumes")
    uploaded_files = st.file_uploader("Upload PDF files", type=["pdf"], accept_multiple_files=True)

with col2:
    if uploaded_files and job_description:
        st.header("Ranking Resumes")
        resumes = []
        for file in uploaded_files:
            text = extract_text_from_pdf(file)
            resumes.append(text)

        scores = rank_resumes(job_description, resumes)
        results = pd.DataFrame({"Resume": [file.name for file in uploaded_files], "Score": scores})
        results = results.sort_values(by="Score", ascending=False)

        st.dataframe(results, height=200)

        # Major Skills Extraction and Analysis
        all_skills = extract_major_skills(resumes)
        skill_counts = Counter(all_skills)

        # Skills Pie Chart
        st.header("Major Skills Overview")
        if skill_counts:
            fig, ax = plt.subplots(figsize=(4, 4))
            ax.pie(skill_counts.values(), labels=skill_counts.keys(), autopct='%1.1f%%', startangle=90, textprops={'fontsize': 8})
            ax.axis('equal')
            st.pyplot(fig)
        else:
            st.write("No major skills found.")

        # Stats Bar
        st.header("Resume Analysis Statistics")
        col1_stats, col2_stats, col3_stats = st.columns(3)
        col1_stats.metric("Total Resumes", len(uploaded_files))
        col2_stats.metric("Average Score", f"{results['Score'].mean():.2f}")
        col3_stats.metric("Top Score", f"{results['Score'].max():.2f}")