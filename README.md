# AI_resume_analyzer
# 🤖 AI Resume Analyzer

An AI-powered web application that analyzes resumes against job descriptions and provides actionable career insights.

## 🚀 Project Overview

AI Resume Analyzer is a Flask-based web application designed to help job seekers understand how well their resume matches a particular job description.

The application analyzes:

- Resume skills
- Job-description skills
- Keyword coverage
- Text relevance
- ATS compatibility
- Matched skills
- Missing skills
- Resume structure
- AI-generated recommendations
- Analysis history

## ✨ Features

### 📊 Resume Match Analysis

Provides an overall resume-to-job match score based on multiple analysis metrics.

### 🎯 Skill Matching

Identifies:

- Matched skills
- Missing skills
- Technical skills
- Job-specific requirements

### 🔑 Keyword Intelligence

Detects important keywords from the job description and checks their presence in the resume.

### 🧠 Text Relevance

Uses text-processing techniques to compare resume content with the job description.

### 🤖 ATS Analysis

Checks important resume sections and evaluates ATS compatibility.

### 💡 AI Career Insights

Provides recommendations based on detected missing skills and resume-job alignment.

### 📈 Analysis Dashboard

Displays:

- Overall Match
- Skill Match
- Text Relevance
- Keyword Coverage
- ATS Compatibility

### 🕒 Analysis History

Stores previous analysis results so users can review earlier evaluations.

### 📄 PDF Resume Parsing

Extracts text from uploaded PDF resumes for analysis.

## 🛠️ Technology Stack

### Backend

- Python
- Flask

### Frontend

- HTML5
- CSS3
- JavaScript

### NLP / Analysis

- Python NLP techniques
- TF-IDF
- Cosine Similarity
- Keyword extraction
- Skill matching

### Data

- SQLite

### PDF Processing

- PyPDF

## 📁 Project Structure

```text
AI_resume_analyzer/
│
├── analyzer/
│   ├── ats_analyzer.py
│   ├── matcher.py
│   ├── recommendations.py
│   ├── resume_parser.py
│   └── skill_extractor.py
│
├── database/
│
├── reports/
│
├── static/
│   ├── CSS/
│   ├── JS/
│   ├── images/
│   └── script.js
│
├── templates/
│   ├── index.html
│   ├── dashboard.html
│   ├── history.html
│   └── analysis_detail.html
│
├── uploads/
├── app.py
├── requirements.txt
└── README.md
