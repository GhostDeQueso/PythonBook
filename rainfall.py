def main():

    months = ['Jan', 'Feb', 'March', 'April', 'May', 'Jun', 'Jul', 'Aug' 
              ,'Sep', 'Oct', 'Nov', 'Dec' ]
    
    amount_of_months = 0
    numbers = []

    for month in months:
        amount_of_months += 1
        print(f"{month}: ", end="")
        rain = int(input())
        numbers.append(rain)


    total_nr = total(numbers)
    print(f"The total is: {total_nr}")

    average = avg(total_nr, amount_of_months)
    print(average)

    the_lowest, the_highest = low_high(numbers)
    print("the lowest nr is: ", the_lowest)
    print("the highest nr is: ", the_highest)



def total(numbers):
    total = 0
    for number in numbers:
        total += number
    return total
        

def avg(total_nr, amount_of_months):
    average = total_nr / amount_of_months
    return average

def low_high(numbers):
    numbers.sort()
    the_lowest = numbers[0]
    the_highest = numbers[-1]


    return the_lowest, the_highest
    


main()