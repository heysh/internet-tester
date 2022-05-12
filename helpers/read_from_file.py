from datetime import datetime
import csv
from config import INTERNET_RESULTS_FILE, PING_RESULTS_FILE

def read_from_file(internet=True):
    timestamp_list, ping_list, download_list, upload_list = [], [], [], []
    file = INTERNET_RESULTS_FILE if internet else PING_RESULTS_FILE

    with open(file, "r") as f:
        reader = csv.reader(f)

        for (index, row) in enumerate(reader):
            if index == 0:
                continue

            timestamp_list.append(row[0])
            ping_list.append(row[1])

            if internet:
                download_list.append(row[2])
                upload_list.append(row[3])

    timestamp_list = [datetime.strptime(x, "%Y-%m-%d %H:%M:%S") for x in timestamp_list]
    ping_list = [float(x) for x in ping_list]

    if internet:
        download_list = [float(x) for x in download_list]
        upload_list = [float(x) for x in upload_list]

    return (timestamp_list, ping_list, download_list, upload_list) if internet else (timestamp_list, ping_list)