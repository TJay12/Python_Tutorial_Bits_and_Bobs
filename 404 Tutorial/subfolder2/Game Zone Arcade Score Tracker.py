# Functions
def get_name():
    name = input("Enter Name")
    return name

def get_valid_score(game_name):
    while True:
        try:
            score = float(input(f"Enter Score {game_name} (0-100): "))
            if 0 <= score <= 100:
                return score
            else:
                print("Invalid Score, must be 0-100")
        except ValueError:
            print("Invalid input")

def get_achieved_level(average):
    if average >= 90:
        return "Elite"
    elif average >= 75:
        return "Pro"
    elif average >= 60:
        return "Casual"
    else:
        return "Rookie"
# Main
while True:
    print("Welcome")
    player_name = input("Enter Name")
    speedracer_score = get_valid_score("{SpeedR}")
    alien_attack_score = get_valid_score("{AlA}")
    puzzle_master_score = get_valid_score("{PuzM}")

    # Calculate the average
    average = (speedracer_score + alien_attack_score + puzzle_master_score ) / 3
    achievement = get_achieved_level(average)

    # Display Result
    print("--Player Report Score")
    print(f"Player Name: {player_name}")
    print(f"Speedracer: {speedracer_score} Alien Attack: {alien_attack_score} Puzzle Master: {puzzle_master_score}")
    print(f"Average Score: {average:.2f}")
    print(f"Achievement {achievement}")
    print("-----------------------------------------------------------------------------------------------------\n")

    # Again?
    again = input("Again? y/n: ").lower()
    if again != "y":
        print("Thank You")
    break