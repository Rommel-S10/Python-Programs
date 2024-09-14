def arithmetic_arranger(problems, show_answers=False):
    alphabet = 'abcdefghijklmnopkrstuvwxyz'

    if len(problems) > 5:
        return 'Error: Too many problems.'
    for list_of_numbers in problems:
        if "+" not in list_of_numbers and '-' not in list_of_numbers:
            return "Error: Operator must be '+' or '-'."

    for list_of_numbers in problems:
        for numbers in list_of_numbers:
            result = alphabet.find(numbers)
            if result != -1:
                return 'Error: Numbers must only contain digits.'

    all_digits_of_problems = []
    for list_of_numbers in problems:
        currentnumber = ""

        for numbers in list_of_numbers:
            if numbers != ' ' and numbers != '+' and numbers != '-':
                currentnumber += numbers

            elif numbers == '+' or numbers == '-':
                all_digits_of_problems.append(currentnumber)
                currentnumber = ""
            else:
                continue

        all_digits_of_problems.append(currentnumber)
        currentnumber = ""

    for numbers in all_digits_of_problems:
        if len(numbers) >= 5:
            return 'Error: Numbers cannot be more than four digits.'
    first_line = ""
    second_line = ""
    dashes_line = ""
    result_line = ""

    for problem in problems:
        problem = problem.replace(" ", "")
        if '+' in problem:
            first_number, second_number = problem.split("+")
            operator = "+"
            result = str(int(first_number) + int(second_number))
        elif '-' in problem:
            first_number, second_number = problem.split("-")
            operator = "-"
            result = str(int(first_number) - int(second_number))

        greatest_length = max(len(first_number), len(second_number))

        first_line += first_number.rjust(greatest_length + 2) + "    "
        second_line += operator + second_number.rjust(greatest_length + 1) + "    "
        dashes_line += "-" * (greatest_length + 2) + "    "

        if show_answers:
            result_line += result.rjust(greatest_length + 2) + "    "

    arithmetic_format = (first_line.rstrip() + "\n" + second_line.rstrip() + "\n" + dashes_line.rstrip())

    if show_answers:
        arithmetic_format += "\n" + result_line.rstrip()

    return arithmetic_format


print(f'\n{arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True)}')