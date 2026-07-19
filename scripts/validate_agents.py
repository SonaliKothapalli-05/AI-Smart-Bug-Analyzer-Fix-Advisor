from app.triage_agent import TriageAgent
from app.log_agent import LogAnalysisAgent

# Initialize Agents
triage = TriageAgent()
log = LogAnalysisAgent()

# -----------------------------
# Validation Dataset
# -----------------------------
test_cases = [

    {
        "name": "Login Crash",

        "report": """
Application crashes during login.

Component: Authentication

Stack Trace:
java.lang.NullPointerException
at LoginService.login(LoginService.java:45)
""",

        "severity": "Critical",
        "priority": "P1",
        "component": "Authentication",
        "exception": "NullPointerException"
    },

    {
        "name": "PDF Viewer Crash",

        "report": """
Browser crashes while opening PDF.

Component: PDF Viewer

Stack Trace:
TypeError: this.viewer is null
at PdfViewer.render(viewer.js:214)
""",

        "severity": "Critical",
        "priority": "P1",
        "component": "PDF Viewer",
        "exception": "TypeError"
    },

    {
        "name": "Database Failure",

        "report": """
Database connection failed.

Component: Database

Stack Trace:
java.sql.SQLException
at Database.connect(Database.java:88)
""",

        "severity": "Critical",
        "priority": "P1",
        "component": "Database",
        "exception": "SQLException"
    },

    {
        "name": "Network Timeout",

        "report": """
Request timed out while connecting to server.

Component: Network

Stack Trace:
java.net.SocketTimeoutException
at HttpClient.send(HttpClient.java:51)
""",

        "severity": "Medium",
        "priority": "P2",
        "component": "Network",
        "exception": "SocketTimeoutException"
    },

    {
        "name": "UI Alignment",

        "report": """
Button alignment issue on dashboard.

Component: UI

Expected:
Button should be centered.

Actual:
Button appears slightly shifted.
""",

        "severity": "Low",
        "priority": "P4",
        "component": "UI",
        "exception": "Unknown"
    }

]

# -----------------------------
# Validation
# -----------------------------

correct_triage = 0
correct_log = 0

total = len(test_cases)

print("\n========== VALIDATION ==========\n")

for i, case in enumerate(test_cases, start=1):

    triage_result = triage.analyze(case["report"])
    log_result = log.analyze(case["report"])

    triage_ok = (
        triage_result.severity == case["severity"]
        and
        triage_result.priority == case["priority"]
        and
        triage_result.component == case["component"]
    )

    log_ok = (
        log_result.exception_type == case["exception"]
    )

    if triage_ok:
        correct_triage += 1

    if log_ok:
        correct_log += 1

    print(f"Test Case {i}: {case['name']}")
    print("-" * 60)

    print("Expected Severity :", case["severity"])
    print("Predicted Severity:", triage_result.severity)

    print("Expected Priority :", case["priority"])
    print("Predicted Priority:", triage_result.priority)

    print("Expected Component :", case["component"])
    print("Predicted Component:", triage_result.component)

    print()

    print("Expected Exception :", case["exception"])
    print("Predicted Exception:", log_result.exception_type)

    print()

    print("Triage Result :", "PASS" if triage_ok else "FAIL")
    print("Log Result    :", "PASS" if log_ok else "FAIL")

    print("=" * 60)

# -----------------------------
# Accuracy
# -----------------------------

triage_accuracy = (correct_triage / total) * 100
log_accuracy = (correct_log / total) * 100

print("\n========== FINAL REPORT ==========\n")

print("Total Test Cases :", total)

print()

print("Correct Triage Predictions :", correct_triage)
print("Correct Log Predictions     :", correct_log)

print()

print(f"Triage Accuracy : {triage_accuracy:.2f}%")
print(f"Log Accuracy    : {log_accuracy:.2f}%")
print(f"Average Accuracy: {(triage_accuracy + log_accuracy)/2:.2f}%")