from app.triage_agent import TriageAgent

agent = TriageAgent()

report = """
Chrome crashes while opening PDF preview.

TypeError:
viewer.js:214
"""

result = agent.analyze(report)

print(result)