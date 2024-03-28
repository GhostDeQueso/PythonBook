def main():

    numbers = open('numbers.txt', 'r')
    cal = 0
    counter = 0
    for nr in numbers:
        nr = int(nr)
        counter = counter + 1
        cal += nr

    avg = cal / counter
    print(avg)

main()