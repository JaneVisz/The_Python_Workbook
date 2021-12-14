# 24
# Create a program that reads a duration from the user as a number of days, hours,
# minutes, and seconds. Compute and display the total number of seconds represented
# by this duration.

day = float(input("Input days: "))
hour = float(input("Input hours: "))
minute = float(input("Input minutes: "))
second = float(input("Input seconds: "))

day_to_second = day * 86400
hour_to_second = hour * 3600
minute_to_second = minute * 60

total_seconds = day_to_second + hour_to_second + minute_to_second + second
print("The total number of seconds is: ", total_seconds)
