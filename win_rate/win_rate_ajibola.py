import sys

def win_rate(input_file):
    current_streak = 0
    max_streak = 0
    win_count = 0
    total_count = 0
    with open(input_file, 'r') as file:
        file.readline()
        for line in file:
            total_count += 1
            home, away, result = line.strip().split()
            result_home, result_away = result.split('-')
            team = [home, away]
            result = [result_home, result_away]
            check_team_index = team.index('ABC')
            other_index = len(team) - check_team_index - 1
            if int(result[check_team_index]) > int(result[other_index]):
                win_count += 1
                current_streak += 1 
                if current_streak > max_streak:
                    max_streak = current_streak
            else:
                current_streak = 0
        win_rate_per = win_count / total_count * 100
        print(f'Team win rate is {win_rate_per:.2f}%, and longest winning streak is {max_streak}')
        return 

def main():
    input_file = sys.argv[1]
    win_rate(input_file)

if __name__ == "__main__":
    main()