import sys

def process_binaries(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    # Skip the header and parse the remaining lines
    binaries = []
    for line in lines[1:]:  # Skip header
        parts = line.strip().split()
        binaries.append({"binary": parts[0], "created_at": parts[1], "date": parts[2], "status": parts[3]})
    
    # Remove binaries with "succeeded" or "failed" status
    binaries = [b for b in binaries if b["status"] not in ["succeeded", "failed"]]
    
    # Separate queued binaries and sort them by creation time
    queued_binaries = sorted([b for b in binaries if b["status"] == "queued"], key=lambda x: x["created_at"])
    
    # Get the rest of the binaries (running)
    running_binaries = [b for b in binaries if b["status"] != "queued"]
    
    # Combine queued (sorted) and running binaries
    updated_binaries = queued_binaries + running_binaries
    
    # Write the updated list back to the file
    with open(file_path, 'w') as file:
        file.write("binary created_at date status\n")  # Correcting header format to match input
        for b in updated_binaries:
            line = f'{b["binary"]} {b["created_at"]} {b["date"]} {b["status"]}\n'
            file.write(line)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py file")
        sys.exit(1)

    f = sys.argv[1]
    


    process_binaries(f)
