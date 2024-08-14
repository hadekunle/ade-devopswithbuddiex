import os

os.system('clear')

directory = os.path.dirname(os.path.abspath(__file__))
path = f'{directory}/file'

print('ADE-SOLUTION'.center(30,'-'))

def print_n_lines(n_count):
    cleaned_content = []
    with open(path,'r') as file:
        content = file.readlines()

        if not 1 <= n_count <= len(content):
            print(f'Last N Count should be between 1 and {len(content)}')
            exit()

        cleaned_content = [each.strip() for each in content[-n_count:] ]
    return cleaned_content

def main():    
    n_count = 2
    result = print_n_lines(n_count)
    print(*result, sep='\n')

if __name__ == "__main__":
    main()