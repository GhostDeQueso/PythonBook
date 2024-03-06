
def main():
    amount = float(input("Value of the house: "))
    counting(amount)

def counting(m_amount):
    print("Insurance for $", m_amount - (m_amount * 0.20), sep="")


main()