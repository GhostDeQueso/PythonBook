def main():

    numbers = open('numbers.txt', 'w')

    amount = int(input("How many words: "))
    for w in range(amount):
        words = input("These words: ")
        numbers.write(words + '\n')
       
    numbers.close()

    

main()