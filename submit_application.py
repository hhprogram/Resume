import hashlib, hmac, json, requests

secret = "hg2026_python_engineer@!"
endpoint = "https://howgood-apply-api.howgood.workers.dev/apply"

payload = {
    "name": "Harrison Li",
    "email": "Li.Harrison.h@gmail.com",
    "resume": "https://github.com/hhprogram/Resume/blob/main/Harrison%20-%20Resume%20(2026).pdf",       # URL to your resume
    "location": "Berkeley, CA",     # e.g. "New York, NY"
    "linkedin": "https://linkedin.com/in/liharrisonh",
    "codeLink": "https://github.com/hhprogram/Resume/blob/main/submit_application.py",     # URL to the repo/gist containing THIS script
    "yearsPython": 7,
    "yearsDjango": 2,
    "notes": "Found HowGood on climatebase.org as I search for opportunities leveraging software engineering to nudge society onto a better path."
}

body = json.dumps(payload)
signature = hmac.new(secret.encode(), body.encode(), hashlib.sha256).hexdigest()

resp = requests.post(
    endpoint,
    data=body,
    headers={
        "Content-Type": "application/json",
        "X-HMAC-Signature": signature,
    },
)
print(resp.status_code, resp.json())
