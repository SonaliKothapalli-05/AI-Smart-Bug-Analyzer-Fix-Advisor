# 🐞 AI Smart Bug Analyzer & Fix Advisor

An AI-powered bug analysis system that helps developers analyze software bug reports, retrieve similar historical bugs, classify severity and priority, analyze stack traces, and generate professional PDF reports.

---

## 📖 Overview

Software bug reports often contain inconsistent information, making bug triaging time-consuming. This project leverages **Retrieval-Augmented Generation (RAG)**, semantic search, and intelligent agents to automate the bug analysis process.

The application accepts bug reports and supporting files, retrieves similar historical bugs from a knowledge base, predicts bug severity and priority, analyzes logs and stack traces, and generates a comprehensive PDF report.

---

## ✨ Key Features

- 🔍 Semantic search using Retrieval-Augmented Generation (RAG)
- 🤖 AI-based Bug Triage Agent
- 📄 Stack Trace & Log Analysis
- 📊 Historical Bug Retrieval
- 📑 PDF Report Generation
- 🌐 Responsive Web Interface
- 📂 Upload Bug Reports, Logs & Stack Traces
- ⚡ FastAPI REST API
- 📈 Confidence Score for Predictions

---

## 🛠️ Technology Stack

### Backend
- Python
- FastAPI
- ChromaDB
- Sentence Transformers

### Frontend
- HTML
- CSS
- JavaScript

### Libraries
- ReportLab
- Pydantic
- Uvicorn

---

## 📂 Project Structure

```text
AI-Smart-Bug-Analyzer-Fix-Advisor/
│
├── app/                    # Backend source code
├── frontend/               # HTML, CSS, JavaScript
├── data/
│   ├── raw/
│   ├── processed/
│   └── vector_store/
├── scripts/                # Utility scripts
├── tests/                  # Unit tests
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/SonaliKothapalli-05/AI-Smart-Bug-Analyzer-Fix-Advisor.git
```

### Navigate to the project

```bash
cd AI-Smart-Bug-Analyzer-Fix-Advisor
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Start the FastAPI server

```bash
uvicorn app.main:app --reload
```

### Open in your browser

```
http://127.0.0.1:8000
```

---

## 📥 Inputs

The application accepts:

- Bug Report
- Stack Trace
- Error Log
- Optional Bug Files

---

## 📤 Outputs

The system provides:

- Query Summary
- Top Similar Historical Bugs
- Severity Prediction
- Priority Prediction
- Component Identification
- Exception Type
- Failure Point
- Confidence Score
- Downloadable PDF Report

---

## 🔄 Workflow

1. User submits a bug report.
2. Files are preprocessed.
3. Bug embeddings are generated.
4. Similar bugs are retrieved using RAG.
5. Triage Agent predicts severity, priority, and component.
6. Log Analysis Agent extracts exception details.
7. Results are displayed.
8. A PDF report can be downloaded.

---

## 📊 Dataset

This project uses bug reports derived from the **DeepTriage** dataset.

> **Note:** The original `deep_data.csv` dataset is not included because it exceeds GitHub's 100 MB file size limit. Sample datasets are included for demonstration.

---

## 📸 Screenshots

Add screenshots of:

- Home Page
- Bug Analysis Results
- Similar Bug Retrieval
- PDF Report

Example:

```text
screenshots/
├── home.png
├── analysis.png
└── report.png
```

---

## 🚀 Future Enhancements

- Multi-Agent Collaboration
- Root Cause Prediction
- Automatic Fix Suggestions
- Duplicate Bug Detection
- Bug Assignment Recommendation
- LLM Integration
- Cloud Deployment
- Docker Support

---

## 👩‍💻 Author

**Sonali Kothapalli**

GitHub:  
https://github.com/SonaliKothapalli-05

---

## 🙏 Acknowledgements

- FastAPI
- ChromaDB
- Sentence Transformers
- ReportLab
- DeepTriage Dataset

---

## 📄 License

This project is developed for educational and research purposes.
