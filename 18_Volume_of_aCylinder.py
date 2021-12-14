from math import pi
# 18
# The volume of a cylinder can be computed by multiplying the area of its circular
# base by its height. Write a program that reads the radius of the cylinder, along with
# its height, from the user and computes its volume. Display the result rounded to one
# decimal place.

r = float(input("Enter any radius of the cylinder: "))
h = float(input("Enter any height of the cylinder: "))
volume = pi * pow(r, 2) * h
print("The volume of the cylinder is %.1f: " % volume)
