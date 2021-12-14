# 45
# Positions on a chess board are identified by a letter and a number. The letter identifies
# the column, while the number identifies the row, as shown below:
# (the picture of chessboard)
# Write a program that reads a position from the user. Use an if statement to deter-
# mine if the column begins with a black square or a white square. Then use modular
# arithmetic to report the color of the square in that row. For example, if the user enters
# a1 then your program should report that the square is black. If the user enters d5
# then your program should report that the square is white. Your program may assume
# that a valid position will always be entered. It does not need to perform any error
# checking.

position = input("Enter the position: ")

letter = position[0]
number = int(position[1])

if number % 2 == 0:
    state_number = "even"
else:
    state_number = "add"

if ((letter == 'a' or letter == 'c' or letter == 'e' or letter == 'g') and state_number == "add")\
        or ((letter == 'b' or letter == 'd' or letter == 'f' or letter == 'h') and state_number == "even"):
    print("The square is black")
else:
    print("The square is white")

