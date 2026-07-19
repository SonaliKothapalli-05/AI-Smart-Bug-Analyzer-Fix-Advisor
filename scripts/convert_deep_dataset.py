import pandas as pd

# Number of bug reports to import
LIMIT = 500

print("Loading DeepTriage dataset...")

df = pd.read_csv("data/raw/deep_data.csv", nrows=LIMIT)

df = df.fillna("")

new_df = pd.DataFrame({
    "bug_id": df["issue_id"],
    "title": df["issue_title"],
    "description": df["description"],

    # Keep these empty because the dataset doesn't have them
    "stack_trace": "",
    "severity": "",
    "priority": "",
    "component": "Chromium",
    "resolution": "",
    "status": "Open",

    # Extra fields from DeepTriage
    "owner": df["owner"],
    "reported_time": df["reported_time"]
})

new_df.to_csv("data/raw/sample_bugs.csv", index=False)

print(f"Successfully created sample_bugs.csv with {len(new_df)} bug reports.")