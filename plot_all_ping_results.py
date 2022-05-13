from datetime import datetime
from helpers import read_from_file, plot_results

def main():
    results = read_from_file(internet=False)
    file_name = "images/ping-overall/ping_overall_" + datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".png"
    plot_results(results[0], results[1], file_name)

if __name__ == "__main__":
    main()