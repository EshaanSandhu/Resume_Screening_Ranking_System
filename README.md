# AI-Powered Resume Screening and Ranking System

This repository contains the code and resources for an AI-powered resume screening and ranking system. The system leverages natural language processing (NLP) and machine learning (ML) techniques to automate the process of reviewing resumes, extracting relevant information, and ranking candidates based on their suitability for a given job description.

## Table of Contents

* [Features](#features)
* [Technologies Used](#technologies-used)
* [Installation](#installation)
* [File Structure](#file-structure)
* [Future Improvements](#future-improvements)

## Features

* **Automated Resume Parsing:** Extracts key information from resumes.
* **Skill Matching:** Matches candidate skills with job requirements, considering both exact matches and semantic similarities.
* **Ranking and Scoring:** Ranks candidates based on their overall fit, providing a score for each applicant.
* **Keyword Extraction:** Identifies important keywords within resumes and job descriptions.
* **Scalable Architecture:** Designed for efficient processing of large volumes of resumes.
* **Visualization:** Generates visualizations to summarize key insights.

## Technologies Used

* **Python:** The primary programming language.
* **Natural Language Processing (NLP):**
    * NLTK
* **Machine Learning (ML):**
    * Scikit-learn
* **Libraries:**
    * Pandas
    * Regular Expressions (regex)
    * MatplotLib
    * Collections
    * Streamlit
    * PyPDF2
  
## Installation

1.  **Clone the repository:**

    ```bash
    git clone [repository URL]
    cd [repository directory]
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the application (if a web interface is included):**

    ```bash
    python app.py
    ```

## File Structure

.
├── Resume_Ranking.py       # Main Python File
├── Dataset                 # Directory for Sample Resumes
├── requirements.txt        # List of dependencies
├── README.md               # This README file

## Future Improvements

* Integration with applicant tracking systems (ATS).
* Improved semantic matching using advanced NLP models.
* Automated feedback generation for candidates.
* Adding more test cases.
