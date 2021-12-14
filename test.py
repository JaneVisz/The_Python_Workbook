n = int(input("Enter a positive integer: "))
factor = 2

while factor <= n:
    if n % factor == 0:
        n = n / factor
    else:
        factor = factor + 1

print(factor)
