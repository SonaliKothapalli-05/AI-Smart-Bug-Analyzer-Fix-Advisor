# Testing Results

Use these commands for Milestone 1 validation:

```bash
python scripts/prepare_sample_kb.py
pytest
uvicorn app.main:app --reload
```

Manual UI checks:

- Paste a bug report into the text area.
- Upload `.txt` or `.log` files for stack traces and error logs.
- Submit the form and confirm Top-K similar bugs appear.
- Confirm empty submissions return a validation error.

Screenshots should be added after running the UI locally.

