# 25
# In this exercise you will reverse the process described in the previous exercise.
# Develop a program that begins by reading a number of seconds from the user.
# Then your program should display the equivalent amount of time in the form
# D:HH:MM:SS, where D, HH, MM, and SS represent days, hours, minutes and seconds
# respectively. The hours, minutes and seconds should all be formatted so that
# they occupy exactly two digits, with a leading 0 displayed if necessary.

seconds_per_day = 86400
second_per_hour = 3600
second_per_minute = 60

seconds = int(input("Input seconds: "))

days = seconds / seconds_per_day
# zvysok odcitany z poctu dni
seconds = seconds % seconds_per_day

hours = seconds / second_per_hour
# zvysok odcitany z poctu hours
seconds = seconds % second_per_hour

minutes = seconds / second_per_minute
# zvysok odcitany z poctu hours
seconds = seconds % second_per_minute

print("The equivalent duration is", "%d:%0.2d:%0.2d:%0.2d" % (days, hours, minutes, seconds))
