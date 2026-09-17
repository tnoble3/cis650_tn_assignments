def number_to_words(n):
    if not isinstance(n, int) or n < 10 or n > 99:
        return "Error, the input must be a two digit number."

    units = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
             6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
    teens = {11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
             15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
             19: 'nineteen'}
    tens = {10: 'ten', 20: 'twenty', 30: 'thirty', 40: 'forty',
            50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'}

    first_digit = n // 10
    second_digit = n % 10

    if first_digit == 1 and n != 10:
        return teens[n]
    if second_digit == 0:
        return tens[n]
    tens_value = first_digit * 10
    return f"{tens[tens_value]} {units[second_digit]}"

#Hard coded test cases 
if __name__ == "__main__":
    print(number_to_words(13))
    print(number_to_words(48))
    print(number_to_words(20))
    print(number_to_words(10))
    print(number_to_words(99))
    print(number_to_words(11))
    print(number_to_words(100))
    print(number_to_words(9))
    print(number_to_words(-13))
    print(number_to_words(13.5))
    print(number_to_words("13"))