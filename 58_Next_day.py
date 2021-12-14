# 58
# Write a program that reads a date from the user and computes its immediate successor.
# For example, if the user enters values that represent 2013-11-18 then your program
# should display a message indicating that the day immediately after 2013-11-18 is
# 2013-11-19. If the user enters values that represent 2013-11-30 then the program
# should indicate that the next day is 2013-12-01. If the user enters values that represent
# 2013-12-31 then the program should indicate that the next day is 2014-01-01. The
# date will be entered in numeric form with three separate input statements; one for
# the year, one for the month, and one for the day. Ensure that your program works
# correctly for leap years.

import datetime

days = 0

year = int(input('Enter a year: '))
month = int(input('Enter a month: '))
day = int(input('Enter a day: '))
date = datetime.date(year, month, day)
next_day = date + datetime.timedelta(days=1)

print("Entered date is: ", date)
print("Next day is: ", next_day)