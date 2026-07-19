# Raw Dataset Folder

This folder stores historical bug datasets before preprocessing.

Milestone 1 includes `sample_bugs.csv` so the pipeline can be tested immediately. For a larger knowledge base, add exports from:

- Mozilla Bugzilla: https://bugzilla.mozilla.org/rest/
- Apache issue trackers: https://issues.apache.org/
- Eclipse datasets on Kaggle or Eclipse issue exports: https://bugs.eclipse.org/bugs/

Expected columns:

```text
bug_id,title,description,stack_trace,severity,priority,component,resolution,status
```

