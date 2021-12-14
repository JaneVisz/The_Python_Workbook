import math
# or from math import log / log(a)

# 10
# Create a program that reads two integers, a and b, from the user.Your program should
# compute and display:
# • The sum of a and b
# • The difference when b is subtracted from a
# • The product of a and b

a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))
print()
print("The sum of a and b is: ", a + b)
print("The difference when b is substracted from a is: ", a - b)
print("The product of a and b is: ", a * b)
print("The quotient when a is devided by b: ", a / b)
print("The remainder when a is devided by b: ", a % b)
print("The result of log10a: ", math.log10(a))
print("The result of a^b: ", a**b)
