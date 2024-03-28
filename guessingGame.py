import random
def main():
    number = random.randint(1, 10)
    counter = 0

    while True:
        try:
            guess = int(input("Guess the nr from 1 to 100: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue
        counter += 1

        if not count(guess, number):
            print(f"result is {counter}")
            break


def count(guess, number):
    if guess > number and guess <= 100:
        print("Too high")
    elif guess < number and guess >= 1:
        print("Too low")
    elif guess == number:
        print("Congrats")
        return False
    else:
        print("From 1 to 100")
    return True


main()