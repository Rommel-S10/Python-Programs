def arithmetic_arranger(problems, show_answers=False):
    alphabet = 'abcdefghijklmnopkrstuvwxyz'

    if len(problems) > 5: #checks that the list of objects is less than 5
        return 'Error: Too many problems.'

    for list_of_numbers in problems:  #this will check that every object has a + or - operation sign
        if "+" not in list_of_numbers and '-' not in list_of_numbers:
            return "Error: Operator must be '+' or '-'."

    for list_of_numbers in problems:  #this will go through every operator problem
        for numbers in list_of_numbers: # this will go through every number to make sure that is a digit.
            result = alphabet.find(numbers)
            if result != -1: # if it is -1 then it means that a letter was not found
                return 'Error: Numbers must only contain digits. '

    return problems


print(f'\n{arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"])}')