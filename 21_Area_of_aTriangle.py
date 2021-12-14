# 20
# The area of a triangle can be computed using the following formula, where b is the
# length of the base of the triangle, and h is its height:
# area =  (b × h) / 2
# Write a program that allows the user to enter values for b and h. The program
# should then compute and display the area of a triangle with base length b and height h.

base = float(input("Enter the length of the base of the triangle: "))
height = float(input("Enter the length of the height of the triangle: "))

area = (base * height) / 2
print("The area of a triangle is %.2f" % area, "m2")
