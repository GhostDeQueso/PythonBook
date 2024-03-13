def main():
    first = int(input("Frist value: "))
    second = int(input("Second value: "))
    print(twoValue(first, second))


def twoValue(first, second):
    if first > second:
        return first
    elif second > first:
        return second
    else: 
        pass
    
main()