from math import sqrt
# 21
# In the previous exercise you created a program that computed the area of a triangle
# when the length of its base and its height were known. It is also possible to compute
# the area of a triangle when the lengths of all three sides are known. Let s1, s2 and s3
# be the lengths of the sides. Let s = (s1 + s2 + s3)/2. Then the area of the triangle
# can be calculated using the following formula:

# Develop a program that reads the lengths of the sides of a triangle from the user and
# displays its area.


s = input("Enter a three lengths of the sides of the traingle: ").split(' ')
# print(type(s))
# print(s)

s1 = float(s[0])
s2 = float(s[1])
s3 = float(s[2])

# print(s1, s2, s3)
perimeter = s1 + s2 + s3
area = sqrt(perimeter * (perimeter - s1) * (perimeter - s2) * (perimeter - s3))

print("The are of the triangle is: %.2f" % area)
print("The perimeter of the triangle is: %.2f" % perimeter)

