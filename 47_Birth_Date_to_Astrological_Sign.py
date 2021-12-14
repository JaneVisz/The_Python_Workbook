# 47
# The horoscopes commonly reported in newspapers use the position of the sun at the
# time of one’s birth to try and predict the future. This system of astrology divides the
# year into twelve zodiac signs, as outline in the table below:
#
# Zodiac sign           | Date range

# Capricorn             | December 22 to January 19
# Aquarius              | January 20 to February 18
# Pisces                | February 19 to March 20
# Aries                 | March 21 to April 19
# Taurus                | April 20 to May 20
# Gemini                | May 21 to June 20
# Cancer                | June 21 to July 22
# Leo                   | July 23 to August 22
# Virgo                 | August 23 to September 22
# Libra                 | September 23 to October 22
# Scorpio               | October 23 to November 21
# Sagittarius           | November 22 to December 21

# Write a program that asks the user to enter his or her month and day of birth. Then
# your program should report the user’s zodiac sign as part of an appropriate output
# message.

month = input("Enter a month: ")
day = int(input("Enter a day: "))
zodiac_signs = " "

if (month == "December" and day >= 22) or (month == "January" and day <= 19):
    zodiac_sign = "Capricorn"
elif (month == "January" and day >= 20) or (month == "February" and day <= 18):
    zodiac_sign = "Aquarius"
elif (month == "February" and day >= 19) or (month == "February" and day <= 20):
    zodiac_sign = "Pisces"
elif (month == "March" and day >= 21) or (month == "April" and day <= 19):
    zodiac_sign = "Aries"
elif (month == "April" and day >= 20) or (month == "May" and day <= 20):
    zodiac_sign = "Taurus"
elif (month == "May" and day >= 21) or (month == "June" and day <= 20):
    zodiac_sign = "Gemini"
elif (month == "June" and day >= 21) or (month == "July" and day <= 22):
    zodiac_sign = "Cancer"
elif (month == "July" and day >= 23) or (month == "August" and day <= 22):
    zodiac_sign = "Leo"
elif (month == "August" and day >= 23) or (month == "September" and day <= 22):
    zodiac_sign = "Virgo"
elif (month == "September" and day >= 23) or (month == "October" and day <= 22):
    zodiac_sign = "Libra"
elif (month == "October" and day >= 23) or (month == "November" and day <= 21):
    zodiac_sign = "Scorpio"
else:
    zodiac_sign = "Sagittarius"

print("The zordiac sing is: ", zodiac_sign)
