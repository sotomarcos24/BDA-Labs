from concurrent.futures import ThreadPoolExecutor
from queue import Queue
import random
import threading
import time


printers = ["Printer-A", "Printer-B", "Printer-C"]

print_jobs = [
    "invoice_batch.pdf",
    "student_report.docx",
    "sales_chart.xlsx",
    "meeting_notes.pdf",
    "poster_draft.png",
    "research_summary.pdf",
    "attendance_sheet.csv",
    "budget_plan.xlsx",
    "slides_final.pptx",
    "lab_instructions.pdf",
]

message_lock = threading.Lock()


def log(message):
    with message_lock:
        print(message)


def print_file(filename, available_printers):
    start = time.perf_counter()
    try:
        log(f"[WAITING] {filename} is waiting for a printer")
        printer = available_printers.get()
        log(f"[START] {filename} is printing on {printer}")
        time.sleep(random.uniform(0.5, 2.0))
        log(f"Using {printer}, file printed: {filename}")
        end = time.perf_counter()
        elapsed = end - start
        log(f"[DONE] {filename} finished on {printer} in {elapsed}")
    finally:
        available_printers.put(printer)


if __name__ == "__main__":
    available_printers = Queue()

    for printer in printers:
        available_printers.put(printer)

    start = time.perf_counter()

    with ThreadPoolExecutor(max_workers=3) as executor:
        for file in print_jobs:
            executor.submit(print_file, file, available_printers)

    end = time.perf_counter()
    elapsed = end - start
    execution_time = round(elapsed, 2)
    print(f"Execution time: {execution_time}")