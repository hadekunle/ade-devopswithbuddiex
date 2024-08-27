import sys

def sort_disk(log1, log2):
    log2_map = {}
    usage = []
    with open(log2, 'r') as log2_lines, open(log1, 'r') as log1_lines:
        next(log2_lines)
        next(log1_lines)
        for line in log2_lines:
            name, _, space = line.strip().split()
            log2_map[name] = space
        for line in log1_lines:
            name, _, used = line.strip().split()
            if name in log2_map:
                total_space = float(log2_map[name])
                percent = (float(used)/total_space) * 100
                usage.append((name, percent))
    usage = sorted(usage, key = lambda x:x[1])
    for server in usage:
        print(f'{server[0]}: {server[1]:.2f}%')

def main():
    log1 = sys.argv[1]
    log2 = sys.argv[2]
    sort_disk(log1, log2)

    
if __name__ == "__main__":
    main()