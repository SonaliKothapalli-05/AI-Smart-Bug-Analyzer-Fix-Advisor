from app.triage_agent import TriageAgent
from app.log_agent import LogAnalysisAgent


class MultiAgentOrchestrator:

    def __init__(self):
        self.triage_agent = TriageAgent()
        self.log_agent = LogAnalysisAgent()

    def analyze(self, report: str):

        triage = self.triage_agent.analyze(report)

        log = self.log_agent.analyze(report)

        return {
            "triage": {
                "severity": triage.severity,
                "priority": triage.priority,
                "component": triage.component,
                "confidence": triage.confidence,
                "reasoning": triage.reasoning,
            },

            "log_analysis": {
                "exception_type": log.exception_type,
                "failure_point": log.failure_point,
                "affected_code_path": log.affected_code_path,
                "confidence": log.confidence,
                "reasoning": log.reasoning,
            }
        }