# 46
# The year is divided into four seasons: spring, summer, fall and winter. While the
# exact dates that the seasons change vary a little bit from year to year because of the
# way that the calendar is constructed, we will use the following dates for this exercise:

# Season | first day

# spring | March 20
# summer | June 21
# fall | September 22
# winter | December 21

# Create a program that reads a month and day from the user. The user will enter
# the name of the month as a string, followed by the day within the month as an
# integer. Then your program should display the season associated with the date that
# was entered.

month = input("Enter a month: ")
day = int(input("Enter a day: "))
season = ""

if month == "January" or month == "February":
    season = "winter"
elif month == "March":
    if day < 20:
        season = "winter"
    else:
        season = "spring"
elif month == "April" or month == "May":
    season = "spring"
elif month == "June":
    if day < 21:
        season = "spring"
    else:
        season = "summer"
elif month == "Jule" or month == "August":
    season = "summer"
elif month == "September":
    if day < 22:
        season = "summer"
    else:
        season = "fall"
elif month == "October" or month == "November":
    season = "fall"
elif month == "December":
    if day < 21:
        season = "fall"
    else:
        season = "winter"

print("The season is: ", season)
