# 0. Pomocí cyklu for napiš program, který vypíše:
# Řádek 0
# Řádek 1
# Řádek 2
# Řádek 3
# Řádek 4

# for rep in range(0, 5):
#     print("Řádek", rep)

# 1. Pomocí cyklu for napiš program, který vypíše:
# 1 na druhou je 1
# 2 na druhou je 4
# 3 na druhou je 9
# 4 na druhou je 16

# for rep in range(1, 5):
#     print(rep, "na druhou je", rep**2)

# 2. Pomocí cyklů for a parametru end pro print napiš program, který postupně z jednotlivých 'X' vypíše:
# X X X X X
# X X X X X
# X X X X X
# X X X X X
# X X X X X

# for i in range(1, 6):
#     for rep in range(1, 6):
#         print("X", end=" ")
#     print()

# 4.
# Napiš program, který vypíše „tabulku“ s násobilkou.
#
# 1 2 3 4
# 2 4 6 8
# 3 6 9 12
# 4 8 12 16

# for i in range(1, 5):
#     for rep in range(1, 5):
#         print(rep*i, end=" ")
#     print()


# 5. Napiš program, který postupně z jednotlivých 'X' vypíše:
#
# X
# X X
# X X X
# X X X X

for cislo_radku in range(5):
    for string in range(cislo_radku):
        print('X', end=' ')
    print()



