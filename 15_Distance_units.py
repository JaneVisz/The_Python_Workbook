# 15
# In this exercise, you will create a program that begins by reading a measurement
# in feet from the user. Then your program should display the equivalent distance in
# inches, yards and miles. Use the Internet to look up the necessary conversion factors
# if you don’t have them memorized.

feet = float(input("Enter a measurement in feets? "))
inches = feet * 12
# approximately the size of quitar
yard = feet / 3
mile = yard / 1760

print("The measurement in feet is: %.2f" % feet, "ft")
print("The measurement in inches is: %.2f" % inches, "inch")
print("The measurement in yards is: %.2f" % yard, "yard")
print("The measurement in miles is: %.2f" % mile, "mile")
