### Session 2 | homework

> In this homework, you will use Gemini API to help fill missing values in a CSV dataset.

#### 1. Goal

You will:

- create a free API key in Google AI Studio
- call Gemini from Python
- load `studio_ghibli_movies.csv`
- build a simple AI-assisted cleaner for missing fields
- save a cleaned dataset to disk

#### 2. Create API key (free)

Go to Google's AI studio, login using your personal gmail and create an API key:

- https://aistudio.google.com/app/api-keys
- Add a name and choose `Default Gemini Project`.
- Copy the API key.

Create a key and keep it private.

Set it in your terminal (macOS/Linux):

```bash
export GEMINI_API_KEY="PASTE_YOUR_KEY"
```

Windows PowerShell:

```powershell
$env:GEMINI_API_KEY="PASTE_YOUR_KEY"
```

#### 3. Limits note

Google AI Studio is free, but it has strict usage limits.

> Gemini 2.0 Flash (the one we will use) on the free tier allows roughly **10–15 requests per minute** and around **200 requests per day**. It supports a large context window, with up to about 1M tokens per minute, making it suitable for experimentation. If you **exceed these limits**, you will receive rate **limit (429) errors**, and usage resets daily. These limits can vary and may change over time.

#### 4. Download dataset

Use: [Birkbeck/studio_ghibli_movies](https://huggingface.co/datasets/Birkbeck/studio_ghibli_movies)

```bash
hf download Birkbeck/studio_ghibli_movies studio_ghibli_movies.csv \
  --repo-type dataset \
  --local-dir .
```

#### 5. Basic Gemini call in Python

Create:

```txt
session2/session_solutions/session-02-homework.py
```

Minimal example:

```python
import json
import os
from urllib.request import Request, urlopen

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise RuntimeError("GEMINI_API_KEY is not set")

url = (
    "https://generativelanguage.googleapis.com/v1beta/models/"
    "gemini-2.0-flash:generateContent?key=" + api_key
)

payload = {
    "contents": [
        {
            "parts": [
                {"text": "In one sentence, what is Studio Ghibli?"}
            ]
        }
    ]
}

request = Request(
    url,
    data=json.dumps(payload).encode("utf-8"),
    headers={"Content-Type": "application/json"},
    method="POST",
)

with urlopen(request, timeout=60) as response:
    data = json.loads(response.read().decode("utf-8"))

text = data["candidates"][0]["content"]["parts"][0]["text"]
print(text)
```

#### 6. Homework exercise (AI-assisted cleaning)

Tasks:

1. Load `studio_ghibli_movies.csv` with `csv.DictReader`.
2. Detect rows with missing `year`.
3. Ask Gemini for the likely release year for each missing movie title.
4. Detect missing `music_by` (`Howl's Moving Castle`).
5. Ask Gemini for the composer name and fill it.
6. Save the cleaned file as `studio_ghibli_movies_ai_clean.csv`.
7. Add a short verification step:
   - print rows still containing empty values
   - print how many values were filled by AI
8. Add a short note in comments:
   - one risk of AI-generated data
   - one way to validate/cross-check results

#### 7. Prompt quality tips

- Ask for one field at a time.
- Ask for strict output format (for example, only the year as 4 digits).
- Keep prompts short and deterministic.
- Add fallback handling if the model returns unexpected output.

#### 8. Share your work

Create a **public GitHub repository** for your coursework. It is better to use one repository for all weekly submissions, for example: `bda-homeworks`.

Include:

- `session2/session_solutions/session-02-homework.py`
- optional: `studio_ghibli_movies_ai_clean.csv`

Submission for this homework is to share your repository link in the class [MS Teams discussion forum](https://teams.microsoft.com/l/team/19%3AQLvZizpid98i6iNwF9_ee7RuoAUPC9YsOVoB3Yrq5YY1%40thread.tacv2/conversations?groupId=8b3672d8-2c38-4134-9725-3b779f03c2b0&tenantId=89d07f47-d258-463c-8700-635ffaeca38e), so Stelios and the rest of the students can see it.
