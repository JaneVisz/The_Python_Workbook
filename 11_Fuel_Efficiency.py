# 11
# In the United States, fuel efficiency for vehicles is normally expressed in miles-pergallon
# (MPG). In Canada, fuel efficiency is normally expressed in liters-per-hundred
# kilometers (L/100 km). Use your research skills to determine how to convert from
# MPGto L/100 km. Then create a program that reads a value from the user in American
# units and displays the equivalent fuel efficiency in Canadian units.

const = 235.214583

MGP = float(input("Enter fuel efficiency in miles-pergallon (MPG): "))
L_per_sto = const / MGP

print("The fuel efficiency in MPG is: %.2f" % MGP)
print("The fuel efficiency in L/100km is: %.2f" % L_per_sto)
