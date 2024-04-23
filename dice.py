import random
def main():

    numbers_of_throws = int(input("Enter a positive integer: "))

    rolls = roll(numbers_of_throws)
    print(rolls)



def roll(numbers_of_throws):

    list = []
    for times in range(numbers_of_throws):
        throws = random.randint(1,6)
        list.append(throws)
    return list
    


main()