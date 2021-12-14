# 63
# Write a program that displays a temperature conversion table for degrees Celsius and
# degrees Fahrenheit. The table should include rows for all temperatures between 0
# and 100 degrees Celsius that are multiples of 10 degrees Celsius. Include appropriate
# headings on your columns. The formula for converting between degrees Celsius and
# degrees Fahrenheit can be found on the internet..

for celsium in range(0, 100, 10):
    fahrenheit = (celsium * 1.8) + 32
    print(celsium, "degrees Celsius is ", fahrenheit, "degrees Fahrenheit")

