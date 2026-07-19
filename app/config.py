from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
VECTOR_STORE_DIR = DATA_DIR / "vector_store"
FRONTEND_DIR = ROOT_DIR / "frontend"

COLLECTION_NAME = "historical_defects"
EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
FALLBACK_EMBEDDING_DIM = 384
DEFAULT_TOP_K = 5

