from dataclasses import dataclass


@dataclass
class TriageResult:
    severity: str
    priority: str
    component: str
    confidence: float
    reasoning: str


class TriageAgent:

    def analyze(self, report: str) -> TriageResult:

        text = report.lower()

        severity = "Medium"
        priority = "P2"
        component = "General"
        confidence = 0.75
        reasoning = []

        # -------- Severity --------

        if "crash" in text or "fatal" in text:
            severity = "Critical"
            priority = "P1"
            confidence = 0.95
            reasoning.append("Crash detected.")

        elif "exception" in text:
            severity = "High"
            priority = "P1"
            confidence = 0.90
            reasoning.append("Unhandled exception detected.")

        elif "error" in text:
            severity = "Medium"
            priority = "P2"
            confidence = 0.85
            reasoning.append("General error detected.")

        else:
            severity = "Low"
            priority = "P3"
            confidence = 0.70
            reasoning.append("Minor issue.")

        # -------- Component --------

        if "pdf" in text:
            component = "PDF Viewer"

        elif "login" in text:
            component = "Authentication"

        elif "database" in text:
            component = "Database"

        elif "network" in text:
            component = "Networking"

        elif "ui" in text:
            component = "User Interface"

        else:
            component = "General"

        return TriageResult(
            severity=severity,
            priority=priority,
            component=component,
            confidence=confidence,
            reasoning=" ".join(reasoning),
        )