def main():

    content = []

    numbers = open('numbers.txt', 'r')
    
    content = numbers.readlines()

    nr_account = input("Enter a number: ")


    if nr_account + '\n' in content:
        print(f'{nr_account} is in the list')
    else:
        print("The number is not in the file")

    
    numbers.close()


main()