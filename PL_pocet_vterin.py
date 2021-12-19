# Vytvoř funkci pocet_vterin, která bude mít dva argumenty:
# čas v minutách a čas ve vteřinách.
# A bude vracet celkový počet vteřin.
minutes = int(input("Input minutes: "))
seconds = int(input("Input seconds: "))


def count_of_seconds(minutes_param, seconds_param):
    return (minutes_param * 60) + seconds_param


print(count_of_seconds(2, 32))

