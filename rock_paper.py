import random

def main():
    computer = computer_choice()
    user_choice = input("3.., 2.., 1..: ").lower()
    print(computer)
    determinate_winner(computer, user_choice)


def computer_choice():
    choices = {1: 'rock', 2: 'paper', 3: 'scissors'}
    return choices[random.randint(1, 3)]


def determinate_winner(computer, user_choice):
    if user_choice == computer:
        print("It's a tie1")
    elif (user_choice == 'rock' and computer == 'scissors') or \
         (user_choice == 'scissors' and computer == 'paper') or \
         (user_choice == 'paper' and computer == 'rock'):
         print(f"User won {user_choice} beats {computer}")
    else:
         print(f"Computer won! {computer} beats {user_choice}")
    


main()