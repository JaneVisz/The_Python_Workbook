# 43
# It is common for images of a country’s previous leaders, or other individuals of his-
# torical significance, to appear on its money. The individuals that appear on banknotes
# in the United States are listed in Table 2.1.

# Individual            | Amount

# George Washington     | $1
# Thomas Jefferson      | $2
# Abraham Lincoln       | $5
# Alexander Hamilton    | $10
# Andrew Jackson        | $20
# Ulysses S. Grant      | $50
# Benjamin Franklin     | $100

# Write a program that begins by reading the denomination of a banknote from the
# user. Then your program should display the name of the individual that appears on the
# banknote of the entered amount. An appropriate error message should be displayed
# if no such note exists.

banknote = input("Enter some value of dollar banknotes (1$, 2$, $5, 10$, 20$, 50$, $100): ")

if banknote == 1:
    leader = "George Washington"
elif banknote == 2:
    leader = "Thomas Jefferson"
elif banknote == 5:
    leader = "Abraham"
elif banknote == 10:
    leader = "Alexander Hamilton"
elif banknote == 20:
    leader = "Andrew Jackson"
elif banknote == 50:
    leader = "Ulysses S. Grant"
else:
    leader = "Benjamin Franklin"

print("The denomination of a baknote is", leader, "and value of this banknote is", banknote)
