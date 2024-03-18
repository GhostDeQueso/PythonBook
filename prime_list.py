def display():

    for number in range(1, 100):
        if is_prime(number):
            print("Prime:", number)

def is_prime(number):

    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                return False
        else:
            return True
                
    else: 
        return False



    

display()