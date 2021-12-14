# 4
# Create a program that reads the length and width of a farmer’s field from the user in
# feet. Display the area of the field in acres.

const = 4356

width = float(input("Enter the width in feet: "))
length = float(input("Enter the length in feet: "))

area_acres = length * width / const
area_float = "{:.4f}".format(area_acres)

print("The area of a farmer's field is: ", area_float, "acres")




