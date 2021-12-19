# Napiš program, který se ptá uživatele na čísla do té doby, než zadá 0.
# Poté vypíše nejmenší ze zadaných čísel. (Pozor: nula se mezi porovnávaná čísla nepočítá.)
# Nápověda: průběžně stačí ukládat jen údaj, které číslo je aktuálně to nejmenší.
number = 1
smallest_number = 0

while True:
    number = int(input("Input any number: "))
    # first iteration

    if number == 0:
        print("You put the zero, so you are done")
        break

    if smallest_number == 0:
        smallest_number = number
    elif number <= smallest_number:
        smallest_number = number


print(smallest_number)

