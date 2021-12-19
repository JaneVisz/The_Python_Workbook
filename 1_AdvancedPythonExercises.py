# All natural numbers divisible by 5 or 7 less tahn 20 are: [0, 5, 7, 10, 14, 15]
# the sum of these numbers is: 51. In this exercise, we treat zero as a natural number.
# Find the sum of all numbers that are divisible by 5 or 7 less than 100
# present the solution in the form of a function called calculation().
# In response, call calculate() function and print the resutl to the console.

# number = 0
# sum_numbers = 0
#
# for number in range(100):
#     if number % 5 == 0 or number % 7 == 0:
#         sum_numbers = sum_numbers + number
#         print("Numbers that are divisible either 5 ir 7: ", number)
#
# print(sum_numbers)

def calculate():
    numbers = []
    for number in range(100):
        if number % 5 == 0 or number % 7 == 0:
            numbers.append(number)
    total = sum(numbers)
    return total


print(calculate())
