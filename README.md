# Internet Tester

A simple program designed to measure the performance of the current computer's internet connection using Ookla's [Speedtest CLI](https://www.speedtest.net/apps/cli).

The internet connection can be measured and visualised in two separate components:

- the latency and the speeds of the internet connection, and

- the latency of the internet connection exclusively.

## Motivation

Primarily, this has been inspired through experiencing an unstable ping during gaming. Whilst the game servers also trouble my friends' ping values, there are times where I am the only one affected by the issue. Hence, I determined that the cause of the problem was either the game servers, or my internet connection.

Even though I didn't experience any hiccups or issues regarding my internet connection in other aspects of my internet usage, I was pretty confident that it was the culprit. Through the development and application of this program, I was able to measure and visualise my internet connection's latency at different times of the day and conclude that the issue originated from my internet connection.

## Installation

There are a few dependencies that are required in order for the scripts to work.

```console
pip install -r requirements.txt
```

## Usage

There are a total of 4 scripts that can be executed:

- `internet_tester.py` – tests the latency, download, and upload speeds of the internet connection across _n_ trials, saves the results, and plots them to `/images/internet`,

- `plot_all_internet_results.py` – plots a graph showing all internet performance results to `/images/internet-overall`,

- `ping_tester.py` – tests the latency of the internet connection across _m_ trials, saves the results, and plots them to `/images/ping`, and

- `plot_all_ping_results.py` – plots a graph showing all ping performance results to `/images/ping-overall`.

Values _n_ and _m_ can be modified within `config.py` through variables `INTERNET_TRIALS` and `PING_TRIALS` respectively.