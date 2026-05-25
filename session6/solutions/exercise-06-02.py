from concurrent.futures import ThreadPoolExecutor
import threading
import time

import requests


call_limit = threading.Semaphore(4)
write_lock = threading.Lock()


def fetch(request_id):
    url = f"https://httpbin.org/delay/1?request={request_id}"

    with call_limit:
        request = requests.get(url, timeout=10)

    with write_lock:
        with open("request_results.txt", "a") as file:
            file.write(f"ID: {request_id}, Status Code: {request.status_code}\n")



if __name__ == "__main__":

    start = time.perf_counter()

    file = open("request_results.txt", "w")
    file.close()

    with ThreadPoolExecutor(max_workers=4) as executor:
        for i in range(1, 41):
            executor.submit(fetch, i)

    end = time.perf_counter()
    print(f"Total time: {end - start:.2f}s")