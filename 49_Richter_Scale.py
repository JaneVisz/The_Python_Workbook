# 49
# The following table contains earthquake magnitude ranges on the Richter scale and
# their descriptors:

# Magnitude            |    Descriptor

# Less than 2.0        |    Micro
# 2.0 to less than 3.0 |    Very minor
# 3.0 to less than 4.0 |    Minor
# 4.0 to less than 5.0 |    Light
# 5.0 to less than 6.0 |    Moderate
# 6.0 to less than 7.0 |    Strong
# 7.0 to less than 8.0 |    Major
# 8.0 to less than 10.0|    Great
# 10.0 or more         |    Meteoric

# Write a program that reads a magnitude from the user and displays the appropriate
# descriptor as part of a meaningful message. For example, if the user enters 5.5 then
# your program should indicate that a magnitude 5.5 earthquake is considered to be a
# moderate earthquake.

magnitude = float(input("Enter an magnitude: "))
descriptor = " "

if magnitude <= 2:
    descriptor = "Micro"
elif 2 < magnitude <= 3:
    descriptor = "Very minor"
elif 3 < magnitude <= 4:
    descriptor = "Minor"
elif 4 < magnitude <= 5:
    descriptor = "Light"
elif 5 < magnitude <= 6:
    descriptor = "Moderate"
elif 6 < magnitude <= 7:
    descriptor = "Strong"
elif 7 < magnitude <= 8:
    descriptor = "Major"
elif 8 < magnitude <= 10:
    descriptor = "Great"
elif magnitude > 10:
    descriptor = "Meteoric"

print("Descriptor: ", descriptor)
