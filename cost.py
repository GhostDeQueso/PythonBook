def main():
    loan = float(input('Your loan payment: '))
    insu = float(input('Your insurance: '))
    gas = float(input('Your gas: '))
    oil = float(input('Your oil: '))
    tiers = float(input('Your tires: '))
    maintenance = float(input('Your maintenance: '))

    total_m = loan + insu + gas + oil + tiers + maintenance
    print('Your montly payment is $', total_m, sep="")
    print('Your montly annual is $', counting(total_m), sep="")


def counting(total_m):
    total_r = total_m * 12
    return total_r

main()





main()