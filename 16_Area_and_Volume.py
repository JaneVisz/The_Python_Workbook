from math import pi
# 16
# Write a program that begins by reading a radius, r , from the user. The program will
# continue by computing and displaying the area of a circle with radius r and the
# volume of a sphere with radius r . Use the pi constant in the math module in your
# calculations.

r = float(input("Enter any value of a radius r: "))
area = pi * pow(r, 2)
volume = (3 / 4) * pi * pow(r, 3)

print("The area of a circle is: %.2f" % area)
print("The volume of circle is: %.2f" % volume)
