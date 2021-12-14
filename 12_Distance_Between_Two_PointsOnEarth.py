from math import pi
from math import sin, cos, acos
# 12
# The surface of the Earth is curved, and the distance between degrees of longitude
# varies with latitude. As a result, finding the distance between two points on the surface
# of the Earth is more complicated than simply using the Pythagorean theorem.
# Let (t1, g1) and (t2, g2) be the latitude and longitude of two points on the Earth’s
# surface. The distance between these points, following the surface of the Earth, in
# kilometers is:
# distance = 6371.01 × arccos(sin(t1) × sin(t2) + cos(t1) × cos(t2) × cos(g1 − g2))
# The value 6371.01 in the previous equation wasn’t selected at random. It is
# the average radius of the Earth in kilometers.
# Create a program that allows the user to enter the latitude and longitude of two
# points on the Earth in degrees. Your program should display the distance between
# the points, following the surface of the earth, in kilometers.

# the function that TRANSFORM DEGREES TO RADIUS
const = 6371.01


def degrees_to_rads(deg):
    return (deg * pi) / 180.0


t1 = float(input("Enter the latitude of the first point on the Earth in degrees: "))
g2 = float(input("Enter the longitude of the second point on the Earth in meters: "))
t2 = float(input("Enter the latitude of the second point on the Earth in degrees: "))
g1 = float(input("Enter the longitude of the first point on the Earth in meters: "))

t1_rad = degrees_to_rads(t1)
t2_rad = degrees_to_rads(t2)
print()
print("The langitude of the first point in radians is: ", t1_rad)
print("The langitude of the second point in radians is: ", t2_rad)

distance = const * acos(sin(t1_rad) * sin(t2_rad) + cos(t1_rad) * cos(t2_rad) * cos(g1 - g2))

print("Distance is: %.2f" % distance, "m")
