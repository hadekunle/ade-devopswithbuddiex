import sys
import pandas as pd


def traffic(data):

    # Create DataFrame
    df = pd.read_csv(data, delim_whitespace=True)

    global cell_summary

    global service_summary

    # Calculate QPS and Throughput per cell
    cell_summary = df.groupby("Cell")[["QPS", "Throughput(Mbps)"]].sum().reset_index()

    # Calculate QPS and Throughput per service
    service_summary = (
        df.groupby("Service")[["QPS", "Throughput(Mbps)"]].sum().reset_index()
    )


def main():

    if len(sys.argv) != 2:
        print("Usage: Python traffic <file>")
        sys.exit(1)

    data = sys.argv[1]
    print(data)

    traffic(data)
    print("QPS and Throughput per Cell:")
    print(cell_summary)
    print("\nQPS and Throughput per Service:")
    print(service_summary)


# Entry point of the program
if __name__ == "__main__":
    main()
