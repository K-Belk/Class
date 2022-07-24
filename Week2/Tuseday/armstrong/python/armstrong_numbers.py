# How can you make this more scalable and reusable later?
def find_armstrong_numbers(numbers):
    armstrong_numbers = []
    for num in numbers:
        checkResults = armstrong_checker(num)
        if checkResults != None:
            armstrong_numbers.append(checkResults)
    return armstrong_numbers

def int_to_list(number):
    # using list comprehension to convert number to list of integers
    return [int(x) for x in str(number)]


def armstrong_checker(number):
    list = int_to_list(number)
    length = len(list)
    armstrong = 0
    for num in list:
        armstrong += num**length
    return armstrong if armstrong == number else None



# print(find_armstrong_numbers([10, 120, 3, 153]))