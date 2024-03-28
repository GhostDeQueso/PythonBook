def main():

    number = open('numbers.txt', 'r')

    read_numbers = number.read()

    number.close()

    print(read_numbers)


main()