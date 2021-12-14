# 72
# A string is a palindrome if it is identical forward and backward. For example “anna”,
# “civic”, “level” and “hannah” are all examples of palindromicwords. Write a program
# that reads a string from the user and uses a loop to determines whether or not it is a
# palindrome. Display the result, including a meaningful output message.

# MY WAY
line = input("Enter a string: ")
# word written on the back
reverse_line = line[::-1]

if reverse_line[:(len(reverse_line)//2)] == line[:(len(line)//2)]:
    print("The string is palindrome.")
else:
    print("The string is not palindrome")

# # THEIR WAY
# line = input("Enter a string: ")
#
# # Assume that it is a palindrome until we ca prove otherwise
# is_palindrome = True
#
# # Check the characters, starting from the ends until the middle is reached
# for i in range(0, len(line) // 2):
#     # if the character dont match then mark that the strig is not palindrome
#     if line[i] != line[len(line) - i - 1]:
#         print(i)
#         is_palindrome = False
#
# print(len(line))
#
#
# # Display a meaningful output message
# if is_palindrome:
#     print(line, "is a palindrome")
# else:
#     print(line, "is not a palindrome")

