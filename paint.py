perH = 35
perH = int(perH)


def main():
    
    square = int(input("Enter square m: "))
    paint = float(input("Enter paint price: "))
    galons = galon(square)
    print("needed galons:", galons)
    hours1 = hours(square)
    print("h of work: ", hours1)
    cost1= cost(paint, square)
    print("Paints cost: ", cost1)
    labor1 = labor(square)
    print("Robocizna:", labor1)
    total(labor1, cost1)

def galon(square):
    galon = square / 112
    return galon

def hours(square):
    per_1_hour = 112 / 8 
    hours = square / per_1_hour 
    return hours

def cost(paint, square):
    galons = galon(square)
    cost = paint * galons
    return cost

def labor(square):
    hours1 = hours(square)
    labor = hours1 * perH
    return labor

def total(labor1, cost1):
    total = labor1 + cost1
    print(total)


    

    

main()