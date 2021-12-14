# 29
# Write a program that begins by reading a temperature from the user in degrees
# Celsius. Then your program should display the equivalent temperature in degrees
# Fahrenheit and degrees Kelvin. The calculations needed to convert between different
# units of temperature can be found on the internet.

celsius = float(input("Enter any temperature in degree Celsius: "))
fahrenheit = 1.8 * celsius + 32
kelvin = celsius + 273
print()
print("Temperature in degrees Celsius is: %.2f" % celsius, "°C")
print("Temperature in degrees Fahrenheit is:  %.2f" % fahrenheit, "F")
print("Temperature in degrees Kelvin is:  %.2f" % kelvin, "K")
