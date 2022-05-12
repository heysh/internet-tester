import speedtest
from datetime import datetime
from helpers import get_results, write_ping_result_to_file, plot_results

def main():
    s = speedtest.Speedtest()
    ping_list = []
    timestamp_list = []

    for i in range(50):
        ping = get_results(s, internet=False)
        ping_list.append(ping)

        timestamp = datetime.strptime(datetime.now().strftime("%Y-%m-%d_%H-%M-%S"), "%Y-%m-%d_%H-%M-%S")
        timestamp_list.append(timestamp)

        write_ping_result_to_file(timestamp, ping)

    file_name = "images/ping/ping_" + datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".png"
    plot_results(timestamp_list, ping_list, file_name)

if __name__ == "__main__":
    main()