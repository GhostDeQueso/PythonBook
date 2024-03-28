def main():

    numbers = open('numbers.txt', 'r')
    cal = 0
    for nr in numbers:
        nr = int(nr)

        cal += nr
    print(cal)

main()