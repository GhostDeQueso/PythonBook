def main():
    name = input("Name of the file: ")
    if name == 'numbers':
        try:
            counter = 0
            with open('numbers.txt', 'r') as numbers:
                for line in numbers:
                    counter += 1
                    print(f"Line {counter} : {line.strip()} ")
        except FileNotFoundError:
            print("File not found. Please make sure the file name is correct and the file exists.")

        numbers.close()           
            
main()