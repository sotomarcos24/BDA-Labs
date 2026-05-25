from concurrent.futures import ThreadPoolExecutor
import threading
import time


door_limit = threading.Semaphore(2)


def enter_room(worker_name):
    print(f"{worker_name} is waiting to enter")

    with door_limit:
        print(f"{worker_name} entered")
        time.sleep(1)
        print(f"{worker_name} left")


if __name__ == "__main__":
    workers = ["Worker A", "Worker B", "Worker C", "Worker D", "Worker E"]

    with ThreadPoolExecutor(max_workers=5) as executor:
        for worker in workers:
            executor.submit(enter_room, worker)