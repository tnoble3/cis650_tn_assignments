from task2a import number_to_words

def interface_simple():
    print("Number to Words Converter")
    print("Enter a two-digit number (10-99) to convert it to words.")
    print("Type 'quit' to exit.\n")

    while True:
        user_input = input("Enter a number (or 'q' to exit): ").strip()
        if user_input.lower() == 'q':
            print("Goodbye!")
            break
        if not user_input.lstrip('-').isdigit():
            print("Error: Please enter a valid whole number.\n")
            continue
        number = int(user_input)
        result = number_to_words(number)
        print(f"Result: {result}\n")

if __name__ == "__main__":
    interface_simple()