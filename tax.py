def main():
    value = int(input('Value of the property: '))
    print(format(property(value), '.2f'), end="")
    print('$')

def property(value):
    accessment = value * 0.6 
    tax(accessment)
    return tax(accessment)
    
    
def tax(value):
    total_tax = value * 0.0072
    return total_tax

main()