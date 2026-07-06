from app.config import DEFAULT_TOP_K
from app.embeddings import get_embedding_service
from app.models import AnalyzeResponse, BugChunk
from app.vector_store import get_vector_store


def index_chunks(chunks: list[BugChunk], reset: bool = False, force_json: bool = False) -> int:
    store = get_vector_store(force_json=force_json)
    if reset:
        store.reset()
    embeddings = get_embedding_service().embed([chunk.text for chunk in chunks])
    store.add(chunks, embeddings)
    return len(chunks)


def retrieve_similar_bugs(text: str, top_k: int = DEFAULT_TOP_K, force_json: bool = False) -> AnalyzeResponse:
    query_text = text.strip()
    if not query_text:
        return AnalyzeResponse(query_summary="", top_k=top_k, matches=[])
    embedding = get_embedding_service().embed([query_text])[0]
    matches = get_vector_store(force_json=force_json).query(embedding, top_k=top_k)
    return AnalyzeResponse(query_summary=query_text[:240], top_k=top_k, matches=matches)

