import random

def main():
    counter = 0
    for _ in range(5):
        counter += 1
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        question = num1 + num2
        print("Question", counter, ": ", sep="", end="")
        print(num1, "+", num2, "=", question)


        
        

main()
    