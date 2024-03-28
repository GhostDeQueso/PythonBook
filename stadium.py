def main():

    cat_a = 20
    cat_b = 15
    cat_c = 10
    cat_a - int(cat_a)
    cat_b - int(cat_b)
    cat_c - int(cat_c)


    amount_a = int(input("how many A: "))
    amount_b = int(input("how many B: "))
    amount_c = int(input("how many C: "))


    total = ticketA(amount_a) + ticketB(amount_b) + ticketC(amount_c)
    print(total)

def ticketA(amount_a):

    ticket = amount_a * 20
    return ticket

def ticketB(amount_b):

    ticket = amount_b * 15
    
    return ticket

def ticketC(amount_c):

    ticket = amount_c * 10
    
    return ticket









main()
    