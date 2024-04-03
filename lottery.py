import random

def main():

    counter = 0
    lottery_list = []
    while counter < 7:
        counter += 1
        numbers = random.randint(0, 9)
        lottery_list.append(numbers)
    print(lottery_list)




main()