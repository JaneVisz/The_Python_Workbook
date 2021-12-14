# 31
# Develop a program that reads a four-digit integer from the user and displays the sum
# of the digits in the number. For example, if the user enters 3141 then your program
# should display 3+1+4+1=9.

four_digit_integer = input("Enter any four-digit integer: ")
first = int(four_digit_integer[0])
second = int(four_digit_integer[1])
third = int(four_digit_integer[2])
fourth = int(four_digit_integer[3])

sum_of_numbers = first + second + third + fourth
print("You entered this number: ", four_digit_integer)
print("The sum of individual numbers is: ", sum_of_numbers)

