import sys
import subprocess

def run_shell(input_file):
    with open(input_file , 'r') as lines:
        for line in lines:
            line = line.strip()
            username, _, score, color = line.split(',')
            if float(score) >= 85:
                print(username, color)

def main():
    input_file = sys.argv[1]
    run_shell(input_file)
    subprocess.run("this-command-does-not-exist &> error_log_aji.txt", shell=True, text=True) 

if __name__ == "__main__":
    main()