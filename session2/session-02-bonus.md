### Session 2 | bonus

> Optional bonus task: connect to a live LLM API and practice complexity analysis with real model calls.

#### 1. Goal

In this bonus, you will:

- call a remote LLM endpoint from terminal and Python
- parse JSON responses
- run O(n) and O(n^2) workflows where the model is used in each step

#### 2. API endpoint

Use the private API URL from the **slides (last slide)**. Do not share that URL publicly.

Quick terminal test:

```bash
curl -sS -X POST "<PASTE_PRIVATE_URL_FROM_LAST_SLIDE>" \
  -H "Content-Type: application/json" \
  -d '{"prompt":"say hi"}'
```

On Windows PowerShell, run it in one line:

```powershell
curl -sS -X POST "<PASTE_PRIVATE_URL_FROM_LAST_SLIDE>" -H "Content-Type: application/json" -d "{\"prompt\":\"say hi\"}"
```

#### 3. Python starter (standard library only)

Create these files:

```txt
session2/session_solutions/session-02-bonus.py
session2/session_solutions/bonus_lib.py
```

Use the same `session_solutions/` folder created in Part 1.

Starter code:

> [!IMPORTANT]
>
> I deployed an open model that goes to sleep 😴 when not in use. The first time you call it, it may take up to 2–3 minutes to wake up, please be patient. Hopefully, someone else has already woken it up before you.

```python
import json
from urllib.request import Request, urlopen

url = "<PASTE_PRIVATE_URL_FROM_LAST_SLIDE>"
payload = {"prompt": "Say hi in one short sentence."}

request = Request(
    url,
    data=json.dumps(payload).encode("utf-8"),
    headers={"Content-Type": "application/json"},
    method="POST",
)

with urlopen(request, timeout=30) as response:
    data = json.loads(response.read().decode("utf-8"))
    print(data)
```

#### 4. Tasks

Use a small value like `n = 4` to avoid too many API calls.

1. Create a list of `n` prompts and send each prompt to the model.
2. Store all model responses in a Python list.
3. O(n) model task:
   - for each response, ask the model: "Does this text mention data quality? Answer yes or no."
   - count how many times the model answers `yes`.
4. O(n) local task:
   - find the longest model response by character length.
   - do not use `len()` for this task.
   - create your own function in `bonus_lib.py`, then import and use it in `session-02-bonus.py`.
5. O(n^2) model task:
   - for every pair of responses `(i, j)`, ask the model: "Are these two responses semantically similar? Answer yes or no."
   - count how many pairs get `yes`.
6. Write a short note explaining:
   - why task 3 is O(n)
   - why task 5 is O(n^2)
   - that network/model latency is separate from algorithmic growth in `n`

#### 5. Optional: Deploy your own LLM on Hugging Face

Do you want to deploy your own LLM model for free on Hugging Face?

- It can be great for learning and small experiments.
- There are no strict classroom API key limits like hosted APIs, but performance/resources can be limited.
- It is usually not suitable for huge tasks.

If you want to try this, contact Stelios.

#### 6. Share your work

Create a **public GitHub repository** for your coursework. It is better to use one repository for all weekly submissions, for example: `bda-homeworks`.

For this bonus, include your files:

- `session2/session_solutions/session-02-bonus.py`
- `session2/session_solutions/bonus_lib.py`

Submission for this bonus is to share your repository link in the class [MS Teams discussion forum](https://teams.microsoft.com/l/team/19%3AQLvZizpid98i6iNwF9_ee7RuoAUPC9YsOVoB3Yrq5YY1%40thread.tacv2/conversations?groupId=8b3672d8-2c38-4134-9725-3b779f03c2b0&tenantId=89d07f47-d258-463c-8700-635ffaeca38e), so Stelios and the rest of the students can see it.
