import random
import math

def getIntInput(text: str, errorMessage: str, default: int = None, min_value: int = -math.inf, max_value: int = math.inf) -> int:
    prompt = f"{text}(Default={default}) " if default > 0 else text
    while True:
        try:
            userInput = input(prompt).strip()
            inputValue = default if default is not None and not userInput else int(userInput)
            if not (min_value <= inputValue <= max_value):
                raise ValueError
            return inputValue
        except ValueError:
            print(errorMessage)


def determine_round_winner(player_choice: str, computer_choice: str, conditions: dict) -> str:
    lose_to, win_against = conditions[player_choice]
    if win_against == computer_choice:
        return "Player"
    elif lose_to == computer_choice:
        return "Computer"
    else:
        return "Tie"



def display_result(cpuScore: int, playerScore: int):
    if cpuScore > playerScore:
        return "Computer wins!"
    elif playerScore > cpuScore:
        return "Player wins!"
    else:
        return "Draw!"


def __main__():
    choices = ["Rock", "Paper", "Scissors"]
    #I made this dictionary to make the code more readable || Choice: [Lose to, Win against]
    conditions = {"Rock": ["Paper", "Scissors"], "Paper": ["Scissors", "Rock"], "Scissors": ["Rock", "Paper"]}

    cpuScore = playerScore = 0
    defaultRounds = 10

    rounds = getIntInput("How many rounds do you want to play?: ", 
                         "Please enter a valid number or leave blank for default value!", defaultRounds, 1)

    for currentRound in range(rounds):
        player_choice = getIntInput("""
            [0] Rock
            [1] Paper
            [2] Scissors
            Choose your move: """, 
            "Please enter a valid number!", -1, 0, 2)
        computer_choice = random.choice(choices)
        
        print(f"\nPlayer chose {choices[player_choice]}, and the computer chose {computer_choice}")
        winner = determine_round_winner(choices[player_choice], computer_choice, conditions)

        if winner == "Tie":
            print("It's a tie!")
        elif winner == "Computer":
            print("Computer won the round!")
            cpuScore += 1
        else:
            print("Player won the round!")
            playerScore += 1

    result = display_result(cpuScore, playerScore)
    print(f"\nGame result: {result}  {cpuScore}-{playerScore}")


if __name__ == '__main__':
    __main__()