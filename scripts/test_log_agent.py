from app.log_agent import LogAnalysisAgent

agent = LogAnalysisAgent()

text = """
Application crashes during login

NullPointerException at LoginService.java:45

at LoginService.login(User.java:45)
"""

result = agent.analyze(text)

print(result)

