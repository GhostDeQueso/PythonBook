def main():
    amountOfLoanA = float(input("Amount of loan in $: "))
    monthlyRateR = float(input("Rate in %: ").replace('%', ''))
    amountOfMonthM = int(input("Amount of monts: "))

    loan(amountOfLoanA, monthlyRateR, amountOfMonthM)
    


def loan(amountOfLoanA, monthlyRateR, amountOfMonthM):

    monthlyRateR_decimal = monthlyRateR / 100
   
    p = (monthlyRateR_decimal * amountOfLoanA) / (1 - (1 + monthlyRateR_decimal) ** (-amountOfMonthM))
    print(f"monthly payment is: $ {p:.2f}")
    


main()