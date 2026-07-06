from app.models import BugRecord
from app.preprocess import chunk_records, clean_text


def test_clean_text_normalizes_whitespace_and_urls():
    assert clean_text("Crash\n\nat https://example.com/x") == "Crash at URL"


def test_chunk_records_preserves_metadata():
    record = BugRecord(
        bug_id="BUG-1",
        title="Crash in PDF viewer",
        description="PDF preview crashes when opening a private window",
        severity="critical",
        priority="P1",
        component="PDF Viewer",
        resolution="FIXED",
        status="RESOLVED",
    )
    chunks = chunk_records([record], max_words=8, overlap=2)

    assert chunks
    assert chunks[0].metadata["bug_id"] == "BUG-1"
    assert chunks[0].metadata["component"] == "PDF Viewer"

