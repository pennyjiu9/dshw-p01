import urllib.request, json

url = "https://api.github.com/repos/pennyjiu9/dshw-p01/actions/runs/26337930077/jobs"
req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json"})
data = json.load(urllib.request.urlopen(req))

for job in data["jobs"]:
    print(f"Job: {job['name']}, Conclusion: {job['conclusion']}")
    for step in job["steps"]:
        icon = "✓" if step["conclusion"] == "success" else "✗" if step["conclusion"] == "failure" else "○"
        print(f"  {icon} {step['name']}: {step['conclusion']}")
        if step["conclusion"] == "failure":
            print(f"    Number: {step['number']}, Started: {step['started_at']}")
