# 13
# Many people think about their height in feet and inches, even in some countries that
# primarily use the metric system. Write a program that reads a number of feet from
# the user, followed by a number of inches. Once these values are read, your program
# should compute and display the equivalent number of centimeters.

feet = float(input("What is your height in feets? "))
inches = feet * 12
cm = inches * 2.54

print("My height in feet is: %.2f" % feet, "ft")
print("My height in inches is: %.2f" % inches, "inch")
print("My height in cm is: %.2f" % cm, "cm")

