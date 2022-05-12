import speedtest
from datetime import datetime
from helpers import get_results, write_internet_results_to_file, plot_results

def main():
    s = speedtest.Speedtest()
    ping_list, download_list, upload_list, timestamp_list = [], [], [], []

    for i in range(5):
        results = get_results(s)

        ping_list.append(results[0])
        download_list.append(results[1] / 1e6)
        upload_list.append(results[2] / 1e6)

        timestamp = datetime.strptime(datetime.now().strftime("%Y-%m-%d_%H-%M-%S"), "%Y-%m-%d_%H-%M-%S")
        timestamp_list.append(timestamp)

        write_internet_results_to_file(timestamp, results)

    file_name = "images/internet/internet_" + datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".png"
    plot_results(timestamp_list, ping_list, file_name, download=download_list, upload=upload_list)

if __name__ == "__main__":
    main()