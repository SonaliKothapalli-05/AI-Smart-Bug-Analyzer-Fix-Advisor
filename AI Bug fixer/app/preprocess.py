import csv
import re
from pathlib import Path

from app.models import BugChunk, BugRecord


SPACE_RE = re.compile(r"\s+")


def clean_text(value: str | None) -> str:
    if not value:
        return ""
    value = value.replace("\x00", " ")
    value = re.sub(r"https?://\S+", " URL ", value)
    value = SPACE_RE.sub(" ", value)
    return value.strip()


def normalize_record(row: dict[str, str]) -> BugRecord:
    return BugRecord(
        bug_id=clean_text(row.get("bug_id")) or clean_text(row.get("id")),
        title=clean_text(row.get("title") or row.get("summary")),
        description=clean_text(row.get("description")),
        stack_trace=clean_text(row.get("stack_trace") or row.get("logs")),
        severity=clean_text(row.get("severity")) or "unknown",
        priority=clean_text(row.get("priority")) or "unknown",
        component=clean_text(row.get("component")) or "unknown",
        resolution=clean_text(row.get("resolution")) or "unresolved",
        status=clean_text(row.get("status")) or "unknown",
    )


def load_bug_csv(path: Path) -> list[BugRecord]:
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    seen: set[str] = set()
    records: list[BugRecord] = []
    for row in rows:
        record = normalize_record(row)
        dedupe_key = record.bug_id or f"{record.title}:{record.description[:80]}"
        if not record.title and not record.description:
            continue
        if dedupe_key in seen:
            continue
        seen.add(dedupe_key)
        if not record.bug_id:
            record.bug_id = f"BUG-{len(records) + 1:05d}"
        records.append(record)
    return records


def chunk_text(text: str, max_words: int = 120, overlap: int = 20) -> list[str]:
    words = text.split()
    if not words:
        return []
    chunks: list[str] = []
    step = max(1, max_words - overlap)
    for start in range(0, len(words), step):
        chunk = words[start : start + max_words]
        if chunk:
            chunks.append(" ".join(chunk))
        if start + max_words >= len(words):
            break
    return chunks


def chunk_records(records: list[BugRecord], max_words: int = 120, overlap: int = 20) -> list[BugChunk]:
    chunks: list[BugChunk] = []
    for record in records:
        for index, text in enumerate(chunk_text(record.searchable_text(), max_words=max_words, overlap=overlap)):
            chunks.append(
                BugChunk(
                    chunk_id=f"{record.bug_id}-{index}",
                    bug_id=record.bug_id,
                    text=text,
                    metadata={
                        "bug_id": record.bug_id,
                        "title": record.title,
                        "component": record.component,
                        "severity": record.severity,
                        "priority": record.priority,
                        "status": record.status,
                        "resolution": record.resolution,
                        "chunk_index": index,
                    },
                )
            )
    return chunks

