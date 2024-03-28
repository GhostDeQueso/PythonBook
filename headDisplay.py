def main():
    while True:
        name = input("Name of the file: ")
        if name == 'numbers':
            numbers = open('numbers.txt', 'r')

            line1 = numbers.readline()
            line2 = numbers.readline()
            line3 = numbers.readline()
            line4 = numbers.readline()
            line5 = numbers.readline()
            

            numbers.close()

            print(line1.rstrip('\n'))
            print(line2.rstrip('\n'))
            print(line3.rstrip('\n'))
            print(line4.rstrip('\n'))
            print(line5.rstrip('\n'))
            
            break


main()