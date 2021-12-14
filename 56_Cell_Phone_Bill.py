# 56
# A particular cell phone plan includes 50 minutes of air time and 50 text messages
# for $15.00 a month. Each additional minute of air time costs $0.25, while additional
# text messages cost $0.15 each. All cell phone bills include an additional charge of
# $0.44 to support 911 call centers, and the entire bill (including the 911 charge) is
# subject to 5 percent sales tax.
# Write a program that reads the number of minutes and text messages used in a
# month from the user. Display the base charge, additional minutes charge (if any),
# additional text message charge (if any), the 911 fee, tax and total bill amount. Only
# display the additional minute and text message charges if the user incurred costs in
# these categories. Ensure that all of the charges are displayed using 2 decimal places.

minutes = int(input("Enter the number of minutes you called this month: "))
messages = int(input("Enter the number of messages you wrote this month: "))
month_tarif = 15
tax_per = 0.05
fee_911 = 0.44

addPrice_messages = 0
addPrice_minutes = 0

if minutes > 50:
    additional_mintes = minutes - 50
    addPrice_minutes = 0.25 * additional_mintes
    print("The additional minute charge is: ", addPrice_minutes, "$")
else:
    addPrice_minutes = 0

if messages > 50:
    additional_messages = messages - 50
    addPrice_messages = 0.15 * additional_messages
    print("The additional messages charge is: ", addPrice_messages, "$")
else:
    addPrice_messages = 0

total_price = month_tarif + addPrice_messages + addPrice_minutes + fee_911
tax_price = total_price * tax_per
total_price = total_price + tax_price

print()
print("The base charge (for 50minutes and 50messages) is: %.2f" % month_tarif, "$")
print("The 911 fee is : %.2f" % fee_911, "$")
print("The tax amount is:  %.2f" % tax_price, "$")
print("Total bill amount is:  %.2f" % total_price, "$")
