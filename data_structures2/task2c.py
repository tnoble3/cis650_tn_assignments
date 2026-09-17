from task2a import number_to_words

def interface_with_memory():
    print("~~~~~ Number to Words Converter (with memory) ~~~~~")
    print("Enter a two-digit number (10-99) to convert it to words.")
    print("Type 'q' to exit.\n")

    cache = {}

    while True:
        user_input = input("Enter a number (or 'q' to exit): ").strip()
        if user_input.lower() == 'q':
            print("Goodbye!")
            break
        if not user_input.lstrip('-').isdigit():
            print("Error: Please enter a valid whole number.\n")
            continue
        number = int(user_input)
        if number in cache:
            print(f"Result (from memory): {cache[number]}\n")
        else:
            result = number_to_words(number)
            cache[number] = result
            print(f"Result (newly computed): {result}\n")


if __name__ == "__main__":
    interface_with_memory()