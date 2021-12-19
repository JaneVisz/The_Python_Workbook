smallest_number = 0
number_of_attempts = 0

while True:
    number = int(input("Enter the number: "))
    number_of_attempts = number_of_attempts + 1

    if number == 0:
        print("You put the zero, so you are done")
        break

    if smallest_number == 0:  # only first iteration
        smallest_number = number
    elif number <= smallest_number:
        smallest_number = number

    # print(smallest_number, number)
print("The number of your attempts is", number_of_attempts, "your the smallest number is: ", smallest_number)

# kom