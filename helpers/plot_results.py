import matplotlib.pyplot as plt

def plot_results(timestamp, ping, file_name, download=None, upload=None):
    if not download and not upload:
        plt.plot(timestamp, ping)
        plt.ylabel("Ping (ms)")

    if download and upload:
        plt.plot(timestamp, ping, label="Ping")
        plt.plot(timestamp, download, label="Download")
        plt.plot(timestamp, upload, label="Upload")
        plt.legend()

    plt.xlabel("Timestamp")
    plt.savefig(file_name)