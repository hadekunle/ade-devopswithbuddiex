import sys

company_number = '(444) 123-1233'


def read_active_users(file_path):
    user_info = {}
    with open(file_path, "r") as activeUsers:
        for line in activeUsers:
            email, area_code, phone_number = line.strip().split()
            username = email.split('@')[0]
            if email.split('@')[1].startswith('yaboo'):
                user_info[username] = f"{area_code} {phone_number}"
    return user_info


def extract_active_user_status(file_path):
    with open(file_path, "r") as user_with_status:
        next(user_with_status)
        return [line.split()[0] for line in user_with_status if line.split()[1].lower() == 'yes']


def main():
    if len(sys.argv) != 3:
        print("Usage: python active_users_finder.py file1 file2")
        sys.exit(1)
    file1 = sys.argv[1]
    file2 = sys.argv[2]

    user_info = read_active_users(file1)
    active_users = extract_active_user_status(file2)

    for username in active_users:
        print(f"{username} {user_info.get(username, company_number)}")


if __name__ == "__main__":
    main()
