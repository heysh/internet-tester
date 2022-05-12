from pathlib import Path
import csv
from config import INTERNET_RESULTS_FILE, PING_RESULTS_FILE

def write_internet_results_to_file(timestamp, results):
    is_file = INTERNET_RESULTS_FILE.is_file()

    with open(INTERNET_RESULTS_FILE, "a", newline="") as f:
        writer = csv.writer(f)

        if not is_file:
            writer.writerow(["Timestamp", "Ping", "Download", "Upload"])

        writer.writerow([timestamp, results[0], results[1] / 1e6, results[2] / 1e6])

def write_ping_result_to_file(timestamp, ping_result):
    is_file = PING_RESULTS_FILE.is_file()

    with open(PING_RESULTS_FILE, "a", newline="") as f:
        writer = csv.writer(f)

        if not is_file:
            writer.writerow(["Timestamp", "Ping"])

        writer.writerow([timestamp, ping_result])