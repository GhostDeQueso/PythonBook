def main():
    fat = float(input("Enter fat grams: "))
    carbo = float(input("Enter carbo grams: "))
    print(count(fat, carbo))

def count(fat, carbo):
    calo1 = fat * 9
    calo2 = carbo * 4
    return calo1, calo2




main()