def main():

    numbers = [74, 19, 105, 20, -2, 67, 77, 124, -45, 38]
    acumulation = 0
    amount = 0
    for number in numbers:
        if number >= 0:
            acumulation += number
            amount += 1
    
    avg = acumulation / amount
    print(avg)


        

main()