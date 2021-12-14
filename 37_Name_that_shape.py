# 37
# Write a program that determines the name of a shape from its number of sides. Read
# the number of sides from the user and then report the appropriate name as part of
# a meaningful message. Your program should support shapes with anywhere from 3
# up to (and including) 10 sides. If a number of sides outside of this range is entered
# then your program should display an appropriate error message.

# read the number of sides from the user
nsides = int(input("Enter the number of sides: "))

# Determine the name, leaving it empty if an unsupported numbers of sides was entered
name = ""

if nsides == 3:
    name = "triangle"
elif nsides == 4:
    name = "quadrillateral"
elif nsides == 5:
    name = "pentagon"
elif nsides == 6:
    name = "hexagon"
elif nsides == 7:
    name = "heptagon"
elif nsides == 8:
    name = "hectagon"
elif nsides == 9:
    name = "nanogon"
elif nsides == 10:
    name = "decagon"

# display an error message or the name of the polygon
if name == "":
    print("That number of sides is not suported by this program")
else:
    print("That is a ", name)

# The empty string is being used as a sentinel value. If
# the number of sides entered by the user is outside of the
# supported range then name will remain empty, causing an error
# message to be displayed later in the program.
