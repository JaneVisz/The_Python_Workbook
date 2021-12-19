# Napiš funkci, která s pomocí cyklu for a příkazu if vypíše z jednotlivých 'X' a mezer následující obrazec:
#
# X X X X X X
# X         X
# X         X
# X         X
# X         X
# X X X X X X

number_x_param = 6

for row in range(number_x_param):
    if row == number_x_param - 1 or row == 0:
        for column in range(number_x_param):
            print("X", end=' ')
        print()
    else:
        print("{:10}".format("X") + "X")

