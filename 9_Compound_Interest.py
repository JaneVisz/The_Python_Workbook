# 9
# Pretend that you have just opened a new savings account that earns 4 percent interest
# per year. The interest that you earn is paid at the end of the year, and is added
# to the balance of the savings account. Write a program that begins by reading the
# amount of money deposited into the account from the user. Then your program should
# compute and display the amount in the savings account after 1, 2, and 3 years. Display
# each amount so that it is rounded to 2 decimal places.

my_deposit = 3445.76

deposit_firstYear = my_deposit + (0.04 * my_deposit)
deposit_secondYear = deposit_firstYear + (0.04 * deposit_firstYear)
deposit_thirdYear = deposit_secondYear + (0.04 * deposit_secondYear)

print("My deposit in first year is: %.2f" % deposit_firstYear)
print("My deposit in second year is:  %.2f" % deposit_secondYear)
print("My deposit in third year is:  %.2f" % deposit_thirdYear)
