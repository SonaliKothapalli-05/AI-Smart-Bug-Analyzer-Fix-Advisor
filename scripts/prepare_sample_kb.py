import json
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from app.config import PROCESSED_DATA_DIR, RAW_DATA_DIR
from app.preprocess import chunk_records, load_bug_csv
from app.rag import index_chunks


def main() -> None:
    source = RAW_DATA_DIR / "sample_bugs.csv"
    records = load_bug_csv(source)
    chunks = chunk_records(records)

    PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)
    (PROCESSED_DATA_DIR / "cleaned_bugs.json").write_text(
        json.dumps([record.model_dump() for record in records], indent=2),
        encoding="utf-8",
    )
    (PROCESSED_DATA_DIR / "chunked_documents.json").write_text(
        json.dumps([chunk.model_dump() for chunk in chunks], indent=2),
        encoding="utf-8",
    )

    count = index_chunks(chunks, reset=True)
    print(f"Indexed {count} chunks from {len(records)} bug records.")


if __name__ == "__main__":
    main()
