from app.models import BugChunk
from app.rag import index_chunks, retrieve_similar_bugs


def test_json_vector_store_retrieves_similar_bug(tmp_path, monkeypatch):
    monkeypatch.setattr("app.vector_store.VECTOR_STORE_DIR", tmp_path)
    chunks = [
        BugChunk(
            chunk_id="BUG-1-0",
            bug_id="BUG-1",
            text="PDF viewer crashes with TypeError while rendering preview",
            metadata={"bug_id": "BUG-1", "title": "PDF crash", "component": "PDF Viewer"},
        ),
        BugChunk(
            chunk_id="BUG-2-0",
            bug_id="BUG-2",
            text="Dark theme contrast issue in marker labels",
            metadata={"bug_id": "BUG-2", "title": "Theme contrast", "component": "UI"},
        ),
    ]

    index_chunks(chunks, reset=True, force_json=True)
    response = retrieve_similar_bugs("PDF preview TypeError crash", top_k=1, force_json=True)

    assert response.matches
    assert response.matches[0].bug_id == "BUG-1"

