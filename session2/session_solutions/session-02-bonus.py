import json
from urllib.request import Request, urlopen

from bonus_lib import my_char_len

# Use the private API URL from the last slide of the module.
# Do not share this URL publicly.
URL = "<PASTE_PRIVATE_URL_FROM_LAST_SLIDE>"


def call_llm(prompt):
    if not URL.startswith("http"):
        raise SystemExit(
            "Set URL to the private endpoint from the last slide before running this script."
        )

    request = Request(
        URL,
        data=json.dumps({"prompt": prompt}).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urlopen(request, timeout=60) as response:
        return json.loads(response.read().decode("utf-8"))


def extract_text(reply):
    if isinstance(reply, dict):
        for key in ("response", "text", "message", "output"):
            if key in reply:
                return str(reply[key])
    return str(reply)


def ask_yes_no(prompt):
    raw = call_llm(prompt)
    text = extract_text(raw).strip().lower()
    return text.startswith("yes")


# Keep n small to avoid many calls.
prompts = [
    "In one sentence, explain why data quality matters.",
    "Give one short tip for cleaning CSV data.",
    "In one sentence, explain a common bug with missing values.",
    "Give one short tip for validating rows in a dataset.",
]

# Task 1-2: O(n) calls to generate responses.
responses = []
for prompt in prompts:
    raw = call_llm(prompt)
    responses.append(extract_text(raw))

print("Collected responses:")
for i, response in enumerate(responses, start=1):
    print(f"{i}. {response}")

# Task 3: O(n) model task (n additional model calls).
data_quality_yes = 0
for response in responses:
    judge_prompt = (
        "Answer with exactly yes or no. "
        "Does the following text mention data quality?\n\n"
        f"Text: {response}"
    )
    if ask_yes_no(judge_prompt):
        data_quality_yes += 1

print("\nTask 3 - Model says 'yes' for data quality:", data_quality_yes)

# Task 4: O(n) local task.
longest_response = ""
for response in responses:
    if my_char_len(response) > my_char_len(longest_response):
        longest_response = response

print("\nTask 4 - Longest response:")
print(longest_response)
print("Task 4 - Character length (custom):", my_char_len(longest_response))

# Task 5: O(n^2) model task (pairwise judge).
similar_pairs_yes = 0
for i in range(len(responses)):
    for j in range(i + 1, len(responses)):
        pair_prompt = (
            "Answer with exactly yes or no. "
            "Are these two texts semantically similar?\n\n"
            f"Text A: {responses[i]}\n"
            f"Text B: {responses[j]}"
        )
        if ask_yes_no(pair_prompt):
            similar_pairs_yes += 1

print("\nTask 5 - Similar response pairs (yes):", similar_pairs_yes)

print("\nComplexity notes:")
print("- Task 3: O(n) model calls")
print("- Task 4: O(n) local scan")
print("- Task 5: O(n^2) model calls")
print("- Network/model latency is external cost; complexity tracks growth with n.")
