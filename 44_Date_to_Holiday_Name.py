# 44
# Canada has three national holidays which fall on the same dates each year.

# Holiday           | Date

# New year’s day    | January 1
# Canada day        | July 1
# Christmas day     | December 25

# Write a program that reads a month and day from the user. If the month and day
# match one of the holidays listed previously then your program should display the
# holiday’s name. Otherwise your program should indicate that the entered month and
# day do not correspond to a fixed-date holiday.

date = input("Enter the month and the day that match one of the holidays for Canada: ")
holiday = ""

if date == "January 1":
    holiday = "New year’s day"
    print(holiday)
elif date == "July 1":
    holiday = "Canada day"
    print(holiday)
elif date == "December 25":
    holiday = "Christmas day"
    print(holiday)

# display an error message or the day of the holidays for Canada
if date == "":
    print("The entered month and day do not correspond to a fixed-date holiday.")
else:
    print(date, "is", holiday)



