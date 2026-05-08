import os

from google import genai


MODEL_NAME = "gemini-2.5-flash"
TEXT_FILE = "les_miserables.txt"
CHUNK_SIZE = 30
MAX_CHUNKS = 3


def ask_gemini(prompt):
    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
    response = client.models.generate_content(model=MODEL_NAME, contents=prompt)
    return response.text


def book_chunks(path, chunk_size=30, max_chunks=3):
    chunk = []
    chunks_sent = 0

    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line == "":
                continue

            # Provide here your solution
            ...

    # Provide here your solution
    ...


def build_summary_prompt(chunk_text, chunk_number):
    # Provide here your solution
    ...


for chunk_number, chunk_text in enumerate(
    book_chunks(TEXT_FILE, chunk_size=CHUNK_SIZE, max_chunks=MAX_CHUNKS),
    start=1,
):
    prompt = build_summary_prompt(chunk_text, chunk_number)
    summary = ask_gemini(prompt)
    print(f"Chunk {chunk_number}")
    print(summary)
    print()