import sys

#A function that accepts both files and returns a list of active users with their phone numbers 
def read_files(fileA, fileB):
    yaboo_users = {}
    #open FileA to identify only yaboo users
    with open(fileA, 'r') as users_file:
        all_users = users_file.readlines()
        for user in all_users:
            user = user.strip('\n')
            email, area_code, phone_number = user.split()
            username, domain = email.split('@')
            sub_domain, top_level_domain = domain.split('.')
            if sub_domain == 'yaboo':
                yaboo_users[username] = (area_code + ' '+ phone_number)

    #open FileB to identify active users
    with open(fileB, 'r') as user_status:
        all_active_users = []
        user_status.readline()
        all_status = user_status.readlines()
        for user in all_status:
            user = user.strip('\n')
            username, status = user.split()
            if status == 'Yes':
                all_active_users.append(username)
    
    #loop through active users and return their phone numbers
    for username in all_active_users:
        if username in yaboo_users.keys():
            print(username, yaboo_users[username])
        else:
            print(username, '(444) 123-1233')

def main():
    fileA = sys.argv[1]
    fileB = sys.argv[2]
    read_files(fileA, fileB)



if __name__ == "__main__":
    main()