def main():

    golf = open('numbers.txt', 'w')

    for i in range(5):
        name_and_score = input("Name and score: ")
        result = golf.write(name_and_score + '\n')
    
    golf.close()

    highest_score = 0
    highest_name = ""

    read_golf = open('numbers.txt', 'r')

    for lines in read_golf:
        parts = lines.split()

        if len(parts) == 2:
            name, score = parts

        score = int(score)

        if score > highest_score:
            highest_score = score
            highest_name = name
        
    print(highest_name, highest_score)

    read_golf.close()



main()