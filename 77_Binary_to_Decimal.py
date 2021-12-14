# 77
# Write a program that converts a binary (base 2) number to decimal (base 10). Your
# program should begin by reading the binary number from the user as a string. Then
# it should compute the equivalent decimal number by processing each digit in the
# binary number. Finally, your program should display the equivalent decimal number
# with an appropriate message.

NEW_BASE = 2

num = int(input("Enter a non-negative integer: "))

# generate the binary represetation of num,
# storing it in result
result = ""
q = num

# perform the body of the loop once
r = q % NEW_BASE
result = str(r) + result
q = q // NEW_BASE

# keep on looing until q==0
while q > 0:
    r = q % NEW_BASE
    result = str(r) + result
    q = q // NEW_BASE

# Display the result
print(num, "in Decimal is", result, "in Binary")

