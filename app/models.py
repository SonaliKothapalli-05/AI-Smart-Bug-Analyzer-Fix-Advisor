from dataclasses import asdict, dataclass, field


class ModelDumpMixin:
    def model_dump(self):
        return asdict(self)


@dataclass
class BugRecord(ModelDumpMixin):
    bug_id: str
    title: str
    description: str
    stack_trace: str = ""
    severity: str = "unknown"
    priority: str = "unknown"
    component: str = "unknown"
    resolution: str = "unresolved"
    status: str = "unknown"

    def searchable_text(self) -> str:
        return "\n".join(
            part
            for part in [
                self.title,
                self.description,
                self.stack_trace,
                self.component,
                self.severity,
                self.priority,
                self.resolution,
                self.status,
            ]
            if part
        )


@dataclass
class BugChunk(ModelDumpMixin):
    chunk_id: str
    bug_id: str
    text: str
    metadata: dict[str, str | int | float | bool] = field(default_factory=dict)


@dataclass
class SimilarBug(ModelDumpMixin):
    chunk_id: str
    bug_id: str
    title: str = ""
    component: str = ""
    severity: str = ""
    priority: str = ""
    status: str = ""
    resolution: str = ""
    score: float = 0.0
    text: str = ""


@dataclass
class AnalyzeResponse(ModelDumpMixin):
    query_summary: str
    top_k: int
    matches: list[SimilarBug]
