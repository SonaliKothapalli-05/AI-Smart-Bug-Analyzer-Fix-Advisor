import re
from dataclasses import dataclass


@dataclass
class LogAnalysisResult:
    exception_type: str
    failure_point: str
    affected_code_path: str
    confidence: float
    reasoning: str


class LogAnalysisAgent:

    def analyze(self, text: str) -> LogAnalysisResult:

        text = text.strip()

        # -----------------------------
        # Exception Type
        # -----------------------------
        exception = "Unknown"

        exception_patterns = [
            r"NullPointerException",
            r"IndexOutOfBoundsException",
            r"ArrayIndexOutOfBoundsException",
            r"IOException",
            r"FileNotFoundException",
            r"SQLException",
            r"TimeoutException",
            r"ClassNotFoundException",
            r"IllegalArgumentException",
            r"TypeError",
            r"ValueError",
            r"KeyError",
            r"AttributeError",
        ]

        for ex in exception_patterns:
            if re.search(ex, text, re.IGNORECASE):
                exception = ex
                break

        # -----------------------------
        # Failure Point
        # -----------------------------
        failure = "Unknown"

        match = re.search(r'([\w]+\.java:\d+)', text)

        if match:
            failure = match.group(1)

        # -----------------------------
        # Code Path
        # -----------------------------
        code_path = "Unknown"

        method = re.search(r'at\s+([\w\.]+)', text)

        if method:
            code_path = method.group(1)

        # -----------------------------
        # Confidence
        # -----------------------------
        confidence = 0.60

        if exception != "Unknown":
            confidence += 0.20

        if failure != "Unknown":
            confidence += 0.10

        if code_path != "Unknown":
            confidence += 0.10

        confidence = min(confidence, 0.99)

        # -----------------------------
        # Reasoning
        # -----------------------------
        if exception != "Unknown":
            reasoning = f"{exception} detected from submitted stack trace."
        else:
            reasoning = "No recognizable exception found."

        return LogAnalysisResult(
            exception_type=exception,
            failure_point=failure,
            affected_code_path=code_path,
            confidence=round(confidence, 2),
            reasoning=reasoning,
        )