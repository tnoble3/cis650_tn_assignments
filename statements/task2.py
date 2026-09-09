def positiveInteger():
    while True:
        try:
            value = int(input("Please enter a positive integer: "))

        except ValueError:
            print("The number entered is not a valid integer.")
            continue

        if value <= 0:
            print("The number entered must be positive.")
            continue
        
        return value

def printMultiples(number):
    multiple = 0

    while multiple <= 100:
        print(multiple)
        multiple += number

def main():
    number = positiveInteger()
    printMultiples(number)

if __name__ == "__main__":
    main()