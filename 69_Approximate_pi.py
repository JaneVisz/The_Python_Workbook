# 69
# The value of pi can be approximated by the following infinite series:

# Write a program that displays 15 approximations of pi. The first approximation
# shouldmake use of only the first term from the infinite series. Each additional approxi-
# mation displayed by your program should include one more term in the series, making
# it a better approximation of pi than any of the approximations displayed previously.
n = 2
pi = 3

for rep in range(0, 15):
    y = 4 / (n * (n+1) * (n+2))
    print("print y : ", y)
    pi = pi + (y * (-1)**rep)
    print("print pi: ", pi)
    n = n + 2
    print("print n", n)
    print()

print("The result after 15. approximation is: ", pi)




