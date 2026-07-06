# AI-Smart-Bug-Analyzer-Fix-Advisor
AI-powered bug analysis system that uses RAG, semantic search, and LLMs to identify root causes and recommend accurate fixes. It helps developers resolve software issues faster by retrieving similar historical bugs and providing intelligent repair suggestions.
# AI Smart Bug Analyzer & Fix Advisor

Milestone 1 builds the foundation for an AI-based bug analysis system. The app accepts bug reports, converts them into embeddings, stores historical defects in a searchable knowledge base, and retrieves similar bugs through an initial RAG pipeline.

## Features

- Bug submission form for pasted reports, bug files, stack traces, and logs
- FastAPI backend with `/api/analyze`, `/api/ingest`, and `/api/health`
- Dataset preprocessing, chunking, embedding generation, and vector indexing
- ChromaDB support with a deterministic JSON vector-store fallback
- Sample historical defect dataset for local testing
- Milestone documentation in `docs/`

## Project Structure

```text
app/                 FastAPI backend and RAG modules
frontend/            Static bug submission UI
data/raw/            Raw sample and public dataset notes
data/processed/      Generated cleaned/chunked data
data/vector_store/   Generated vector database files
scripts/             Dataset preparation scripts
tests/               Foundation tests
docs/                Milestone 1 documentation
```

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

For a lightweight demo without installing ChromaDB or Sentence Transformers, the fallback vector store and fallback embedder still work. For the full stack, install all requirements and allow the Sentence Transformers model to download on first use.

## Build the Knowledge Base

```bash
python scripts/prepare_sample_kb.py
```

This cleans `data/raw/sample_bugs.csv`, chunks bug records, generates embeddings, and indexes them.

## Run the App

```bash
uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000` in a browser.

## Test

```bash
pytest
```

## Milestone 1 Docs

Start with [docs/milestone-1.md](docs/milestone-1.md).
