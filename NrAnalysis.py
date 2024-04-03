def main():

    counter = 0
    numbers = []

    while counter < 5:
        counter += 1
        print(counter, end=". ")
        number = int(input("Enter a number: "))
        numbers.append(number)

    theLowest, theHighest = low_high(numbers)
    print("The lowest is: ", theLowest)
    print(f'The highest is {theHighest}')

    totka = total(numbers)
    print("the total is:", totka)

    avg = average(totka, counter)
    print(f'the average is: {avg}')
   

def low_high(numbers):
    numbers.sort()
    the_lowest = numbers[0]
    the_highest = numbers[-1]
    return the_lowest, the_highest

def total(numbers):
    total = 0
    for value in numbers:
        total += value
    
    return total

def average(totka, counter):
    avg = totka / counter
    return avg


main()