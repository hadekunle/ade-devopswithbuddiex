def calculate_win_rate_and_streak(records):
    win_count = 0
    total_games = 0
    longest_streak = 0
    current_streak = 0

    for record in records:
        home_team, guest_team, result = record
        home_score, guest_score = map(int, result.split('-'))

        if home_team == "ABC":
            if home_score > guest_score:
                win_count += 1
                current_streak += 1
            else:
                current_streak = 0
        elif guest_team == "ABC":
            if guest_score > home_score:
                win_count += 1
                current_streak += 1
            else:
                current_streak = 0

        total_games += 1
        longest_streak = max(longest_streak, current_streak)

    win_rate = (win_count / total_games) * 100 if total_games > 0 else 0
    return win_rate, longest_streak

def read_records_from_file(filename):
    records = []
    with open(filename, 'r') as file:
        lines = file.readlines()[1:]  # Skip the header
        for line in lines:
            parts = line.strip().split()
            home_team = parts[0]
            guest_team = parts[1]
            result = parts[2]
            records.append((home_team, guest_team, result))
    return records


if __name__ == "__main__":
    
    # File containing game records
    filename = 'win_rate/file'

    # Read records from file
    records = read_records_from_file(filename)

    # Calculate win rate and longest winning streak
    win_rate, longest_streak = calculate_win_rate_and_streak(records)

    print(f"Win rate: {win_rate:.2f}%")
    print(f"Longest winning streak: {longest_streak}")



