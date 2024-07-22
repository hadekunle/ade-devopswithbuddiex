import sys

def traffic_check(input_file):
    cell_map = {}
    service_map = {}
    with open(input_file, 'r') as lines:
        next(lines)
        for line in lines:
            service, cell, qps, throughput = line.strip().split()
            if service not in service_map:
                service_map[service] = [int(qps), int(throughput)]
            else:
                service_map[service][0] += int(qps)
                service_map[service][1] += int(throughput)
            if cell not in cell_map:
                cell_map[cell] = [int(qps), int(throughput)]
            else:
                cell_map[cell][0] += int(qps)
                cell_map[cell][1] +=  int(throughput)
    for key, value in cell_map.items():
        print(f'Cell: {key}, QPS: {value[0]}, Throughput(Mbps): {value[1]}')
    for key, value in service_map.items():
        print(f'Service: {key}, QPS: {value[0]}, Throughput(Mbps): {value[1]}')






def main():
    file = sys.argv[1]
    traffic_check(file)

if __name__ == "__main__":
    main()