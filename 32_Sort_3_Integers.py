# 32
# Create a program that reads three integers from the user and displays them in sorted
# order (from smallest to largest). Use the min and max functions to find the smallest
# and largest values. The middle value can be found by computing the sum of all three
# values, and then subtracting the minimum value and the maximum value.

a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))
c = int(input("Enter the third integer: "))

min_number = min(a, b, c)
max_number = max(a, b, c)
middle_number = (a + b + c) - max_number - min_number
print()
print("The biggest number is: ", max_number)
print("The middle number is: ", middle_number)
print("The smallest number is: ", min_number)
