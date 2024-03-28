def main():

    numbers = open('numbers.txt', 'r')
    avg_acumulator = 0
    current_month = None
    days_count = 0

    for line in numbers:
        split = line.split()
        if len(split) == 2:
            nr, string = split
            nr = int(nr)

        if current_month is None:
            current_month = string

        if current_month == string:
            avg_acumulator += nr
            days_count += 1

        else:
            month_avg = avg_acumulator / days_count
            print(f"Average for {current_month} is {month_avg}")

            avg_acumulator = nr
            days_count = 1
            current_month = string

    if days_count > 0:
        month_avg = avg_acumulator / days_count
        print(f"Average for {current_month} is {month_avg:.1f}")

    numbers.close()


main()