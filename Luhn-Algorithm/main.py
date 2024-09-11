def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]  # Reverse the card number string
    odd_digits = card_number_reversed[::2]  # Get odd-indexed digits

    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2]  # Get even-indexed digits
    for digit in even_digits:
        number = int(digit) * 2
        if number >= 10:
            number = (number // 10) + (number % 10)  # Sum the digits if result is >= 10
        sum_of_even_digits += number

    total = sum_of_odd_digits + sum_of_even_digits
    return total % 10 == 0  # Check if total is divisible by 10 (valid Luhn check)


def main():
    # Use a known valid test card number: Visa test card number (4111 1111 1111 1111)
    card_number = '4111 1111 1111 1111'  # This is a valid test card number

    # Remove any non-numeric characters (dashes and spaces)
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

    # Ensure card_number is valid after removing separators
    if not translated_card_number.isdigit():
        print('INVALID! Card number contains invalid characters after translation.')
        return

    # Verify the card number
    if verify_card_number(translated_card_number):
        print('VALID!')
    else:
        print('INVALID!')


main()
