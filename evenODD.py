import random

def main():
    even = 0
    odd = 0
    for number in range(100):
        numbers = random.randint(1, 100)
        
        if numbers % 2 == 0:
            even += 1
        elif numbers % 2 != 0:
            odd += 1
    print(f"Even: {even}")
    print(f"Odd: {odd}")
    

main()