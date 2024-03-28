def main():

    numbers = open('numbers.txt', 'w')

    amount = int(input("How many words: "))
    for w in range(amount):
        words = input("These words: ")
        numbers.write(words + '\n')
    
    numbers.close()


    rNumbers = open('numbers.txt', 'r')

    word_length = 0
    word_counter = 0
    for lines in rNumbers:
        word_counter += 1
        length = len(lines.strip())
        if length > word_length:
            word_length = length



    print(word_counter)
    print(word_length)



main()