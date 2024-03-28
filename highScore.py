def main():

    highest_score = 0
    highest_name = ""

    numbers = open('numbers.txt', 'r')

    for line in numbers:
        split = line.split()

        if len(split) == 2:
            name, score = split

        score = int(score)

        if score > highest_score:
            highest_score = score
            highest_name = name

    print(highest_name, highest_score)

main()