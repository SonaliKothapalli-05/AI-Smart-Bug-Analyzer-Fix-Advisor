const form = document.querySelector("#bug-form");
const statusEl = document.querySelector("#status");
const resultsEl = document.querySelector("#results");

function setStatus(value) {
  statusEl.textContent = value;
}

function renderMatches(matches) {
  if (!matches.length) {
    resultsEl.innerHTML = '<p class="empty">No similar bugs found. Build the knowledge base with <code>python scripts/prepare_sample_kb.py</code>, then try again.</p>';
    return;
  }

  resultsEl.innerHTML = matches
    .map(
      (match) => `
        <article class="match">
          <h3>${escapeHtml(match.title || match.bug_id || "Historical bug")}</h3>
          <div class="meta">
            <span>${escapeHtml(match.bug_id)}</span>
            <span>${escapeHtml(match.component || "component unknown")}</span>
            <span>${escapeHtml(match.severity || "severity unknown")}</span>
            <span class="score">${Math.round(match.score * 100)}% match</span>
          </div>
          <p class="snippet">${escapeHtml(match.text)}</p>
        </article>
      `
    )
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
  setStatus("Searching");
  resultsEl.innerHTML = "";

  try {
    const response = await fetch("/api/analyze", {
      method: "POST",
      body: new FormData(form),
    });
    const payload = await response.json();
    if (!response.ok) {
      throw new Error(payload.detail || "Request failed");
    }
    renderMatches(payload.matches || []);
    setStatus(`${payload.matches.length} result${payload.matches.length === 1 ? "" : "s"}`);
  } catch (error) {
    resultsEl.innerHTML = `<p class="empty">${escapeHtml(error.message)}</p>`;
    setStatus("Error");
  }
});

