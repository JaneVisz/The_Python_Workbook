# 35
# It is commonly said that one human year is equivalent to 7 dog years. However this
# simple conversion fails to recognize that dogs reach adulthood in approximately two
# years. As a result, some people believe that it is better to count each of the first two
# human years as 10.5 dog years, and then count each additional human year as 4 dog
# years.
# Write a program that implements the conversion from human years to dog years
# described in the previous paragraph. Ensure that your program works correctly for
# conversions of less than two human years and for conversions of two or more human
# years. Your program should display an appropriate error message if the user enters
# a negative number.

human_years = int(input("Enter any human year that would be converted to dog years: "))
dog_years = 0

if human_years < 2:
    dog_years = 10.5 * human_years
elif human_years >= 2:
    dog_years = 10.5 * 2 + (human_years - 2) * 4

# Display an error message
if human_years < 0:
    print("This user entered a negative number.")
else:
    print("The dog years: ", dog_years)
