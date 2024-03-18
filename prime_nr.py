def is_prime():

    number = int(input("Enter a number: "))

    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                print("It's not prime")
                break
        else:
            print("It's prime")
                
    else: 
        print("It's not prime")



    

is_prime()