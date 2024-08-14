global log_content


def parse_log(log_content):
    lines = log_content.strip().split("\n")
    high_usage_servers = []

    for line in lines:
        parts = line.split()
        server_name = parts[0]
        disk_usage_str = parts[3]
        disk_usage = float(disk_usage_str.strip("%"))

        if disk_usage > 85:
            high_usage_servers.append(f"{server_name}, {disk_usage_str}")

    return high_usage_servers


def soln(file):

    with open(file, "r") as file:

        log_content = file.read()

    high_usage_servers = parse_log(log_content)
    for server in high_usage_servers:
        print(server)


if __name__ == "__main__":
    directory_path = "find_disk_full/file"
    soln(directory_path)
