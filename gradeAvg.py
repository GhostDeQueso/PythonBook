def main():

    scoreTime = 5
    totalS = 0

    for score in range(scoreTime):
        testScore = int(input("Test score: "))
        totalS = totalS + testScore

    average1 = calc_average(totalS)
    determine_grade(average1)
    


def calc_average(totalS):
    average = (totalS / 5)
    return average


def determine_grade(average1):
    

    if 90 <= average1 <= 100:
        print("Grade A")
    elif 80 <= average1 <= 89:
        print("Grade B")
    elif 70 <= average1 <= 79:
        print("Grade C")
    elif 60 <= average1 <= 69:
        print("Grade D")
    elif average1 < 60:
        print("Grade F")



main()