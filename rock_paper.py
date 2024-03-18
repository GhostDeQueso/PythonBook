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
        print("It's a tie")
    elif (user_choice == 'rock' and computer == 'scissors'):
        print("Rock smashes scissors")
    elif (user_choice == 'scissors' and computer == 'paper'):
        print("Scissors smashes paper")
    elif (user_choice == 'paper' and computer == 'rock'):
        print("Paper smashes rock")
    

main()