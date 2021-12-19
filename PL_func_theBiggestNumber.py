# Napiš funkci, která vrátí maximální hodnotu ze tří zadaných čísel.
a = int(input("Enter any number: "))
b = int(input("Enter any number: "))
c = int(input("Enter any number: "))


def max_value(a_param, b_param, c_param):
    return max(a_param, b_param, c_param)


print("The biggest number is: ", max_value(a, b, c))

