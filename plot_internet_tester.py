from datetime import datetime
from helpers import read_from_file, plot_results

def main():
    results = read_from_file()
    file_name = "images/internet-overall/internet_overall_" + datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".png"
    plot_results(results[0], results[1], file_name, download=results[2], upload=results[3])

if __name__ == "__main__":
    main()