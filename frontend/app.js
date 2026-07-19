const form = document.querySelector("#bug-form");
const statusEl = document.querySelector("#status");
const resultsEl = document.querySelector("#results");
const sampleButton = document.querySelector("#load-sample");
const reportText = document.querySelector("#report_text");

const summaryCard = document.querySelector("#summary-card");
const summaryText = document.querySelector("#summary-text");
const loader = document.querySelector("#loader");
const triageCard = document.querySelector("#triage-card");
const severityEl = document.querySelector("#severity");
const priorityEl = document.querySelector("#priority");
const componentEl = document.querySelector("#component");
const confidenceEl = document.querySelector("#confidence");
const reasoningEl = document.querySelector("#reasoning");
const logCard = document.querySelector("#log-card");

const exceptionTypeEl = document.querySelector("#exception_type");
const failurePointEl = document.querySelector("#failure_point");
const affectedCodePathEl = document.querySelector("#affected_code_path");
const logConfidenceEl = document.querySelector("#log_confidence");
const logReasoningEl = document.querySelector("#log_reasoning");
const downloadBtn = document.querySelector("#download-report");
let latestAnalysis = null;


const sampleInput = `Title: Browser crash when opening PDF preview in private window
Component: PDF Viewer
Environment: Windows 11, latest browser build

Steps to reproduce:
1. Open a private browsing window.
2. Navigate to a PDF document.
3. Wait for the preview toolbar to load.

Expected result:
The PDF preview should remain open and interactive.

Actual result:
The tab becomes unresponsive and the browser process closes.

Console evidence:
TypeError: this.viewer is null at PdfViewer.render viewer.js:214`;

function setStatus(value) {
  statusEl.textContent = value;
}

function renderMatches(matches) {
  if (!matches.length) {
    resultsEl.innerHTML =
      '<p class="empty">No similar bugs found.</p>';
    return;
  }

  resultsEl.innerHTML = matches
    .map((match) => {

      let color = "#dc3545";

      if (match.score >= 0.80)
        color = "#198754";
      else if (match.score >= 0.60)
        color = "#0d6efd";
      else if (match.score >= 0.40)
        color = "#fd7e14";

      return `
        <article class="match">
          <h3>${escapeHtml(match.title || match.bug_id || "Historical Bug")}</h3>

          <div class="meta">
              <span>🆔 Bug ID: ${escapeHtml(match.bug_id)}</span>

              <span>💻 Component:
              ${escapeHtml(match.component || "Chromium")}</span>

              <span class="score"
              style="background:${color};
              color:white;
              padding:6px 12px;
              border-radius:20px;">
              ⭐ ${Math.round(match.score*100)}% Match
              </span>
          </div>

          <p class="snippet">
          ${escapeHtml(match.text.substring(0,200))}...
          </p>

        </article>
      `;
    })
    .join("");
}

function escapeHtml(value) {
  return String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}

form.addEventListener("submit", async (event) => {

  event.preventDefault();

  const start = performance.now();

  loader.style.display = "block";
  summaryCard.style.display = "none";

  setStatus("Searching...");
  resultsEl.innerHTML = "";

  try {

    const response = await fetch("/api/analyze", {
      method: "POST",
      body: new FormData(form),
    });

    const payload = await response.json();
    latestAnalysis = payload;
    console.log(payload);

    if (!response.ok) {
      throw new Error(payload.detail || "Request failed");
    }

    const end = performance.now();

    loader.style.display = "none";

    summaryCard.style.display = "block";

    summaryText.innerHTML = `
      📄 Indexed Reports : <b>500</b><br>
      📑 Indexed Chunks : <b>619</b><br>
      🔍 Results Retrieved : <b>${payload.matches.length}</b><br>
      ⚡ Search Time : <b>${((end-start)/1000).toFixed(2)} sec</b>
    `;

    // Show Triage Result
if (payload.triage) {
    triageCard.style.display = "block";

    severityEl.textContent = payload.triage.severity;
    priorityEl.textContent = payload.triage.priority;
    componentEl.textContent = payload.triage.component;
    confidenceEl.textContent =
        Math.round(payload.triage.confidence * 100) + "%";
    reasoningEl.textContent = payload.triage.reasoning;
}
if (payload.log_analysis) {

    logCard.style.display = "block";

    exceptionTypeEl.textContent =
        payload.log_analysis.exception_type;

    failurePointEl.textContent =
        payload.log_analysis.failure_point;

    affectedCodePathEl.textContent =
        payload.log_analysis.affected_code_path;

    logConfidenceEl.textContent =
        Math.round(payload.log_analysis.confidence * 100) + "%";

    logReasoningEl.textContent =
        payload.log_analysis.reasoning;
}

renderMatches(payload.matches || []);

    setStatus(`${payload.matches.length} Results`);

  }

  catch(error){

    loader.style.display="none";

    resultsEl.innerHTML =
    `<p class="empty">${escapeHtml(error.message)}</p>`;

    setStatus("Error");

  }

});

sampleButton.addEventListener("click", () => {
  reportText.value = sampleInput;
  reportText.focus();
  setStatus("Sample input loaded");
});

downloadBtn.addEventListener("click", async () => {

    if (!latestAnalysis) {
        alert("Please analyze a bug first.");
        return;
    }

    const report = reportText.value;

    const response = await fetch("/api/report", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            report: report,
            ...latestAnalysis
        })
    });

    if (!response.ok) {
    const error = await response.text();
    console.error(error);
    alert(error);
    return;
}

    const blob = await response.blob();

    const url = window.URL.createObjectURL(blob);

    const a = document.createElement("a");
    a.href = url;
    a.download = "Bug_Analysis_Report.pdf";

    document.body.appendChild(a);
    a.click();
    a.remove();

    window.URL.revokeObjectURL(url);
});
