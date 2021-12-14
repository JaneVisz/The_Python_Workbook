# 6
# The program that you create for this exercise will begin by reading the cost of a meal
# ordered at a restaurant from the user. Then your program will compute the tax and
# tip for the meal. Use your local tax rate when computing the amount of tax owing.
# Compute the tip as 18 percent of the meal amount (without the tax). The output from
# your program should include the tax amount, the tip amount, and the grand total for
# the meal including both the tax and the tip. Format the output so that all of the values
# are displayed using two decimal places.

food = input("Which food would you like to eat (pizza, burger, salat)? ")
if food == "pizza":
    price = 150.98
elif food == "burger":
    price = 140.55
else:
    price = 100.11

# tax-rate 15 %
tax_fraction = 0.15
tax = tax_fraction * price
# tip-rate 18 %
tip_fraction = 0.18
tip = tip_fraction * price

total_price = tax + tip + price

print("The price of", food, "at the beginning: ", price, "kč")
print("Tax:  %0.2f" % tax, "kč")
print("Tip:  %0.2f" % tip, "kč")
print("Grand total:  %0.2f" % total_price, "kč")

