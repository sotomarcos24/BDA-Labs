from concurrent.futures import ThreadPoolExecutor
import threading

from faker import Faker


fake = Faker()
write_lock = threading.Lock()


def generate_phrase():
    return fake.sentence(nb_words=6)


def save_phrase(index):
    phrase = generate_phrase()

    with write_lock:
        with open("generated_phrases.txt", "a") as file:
            file.write(f"Phrase {index}: {phrase}\n\n")


if __name__ == "__main__":
    file = open("generated_phrases.txt", "w")
    file.close()

    with ThreadPoolExecutor(max_workers=10) as executor:
        for i in range(1, 11):
            executor.submit(save_phrase, i)
