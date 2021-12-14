# 8
# INPUT, INT, PRINT

# An online retailer sells two products: widgets and gizmos. Each widget weighs 75
# grams. Each gizmo weighs 112 grams. Write a program that reads the number of
# widgets and the number of gizmos in an order from the user. Then your program
# should compute and display the total weight of the order.

number_of_widgets = int(input("Tell me number of widgets you want to buy: "))
number_of_gizmo = int(input("Tell me number of gizmo you want to buy: "))

widget = 75
gizmo = 112

total_weight = (number_of_widgets * widget) + (number_of_gizmo * gizmo)

print("Total weight of your order is: ", total_weight)

