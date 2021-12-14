# 73
# There are numerous phrases that are palindromes when spacing is ignored. Examples
# include “go dog”, “flee to me remote elf” and “some men interpret nine memos”,
# among many others. Extend your solution to Exercise 72 so that it ignores spacing
# while determining whether or not a string is a palindrome. For an additional challenge,
# extend your solution so that is also ignores punctuation marks and treats uppercase
# and lowercase letters as equivalent.

# few examples: go dog, flee to me remote elf, some men interpret nine memos

line = input("Enter a string: ")
line = line.replace(" ", "")
# word written on the back
reverse_line = line[::-1]

if reverse_line[:(len(reverse_line)//2)] == line[:(len(line)//2)]:
    print("The string is palindrome.")
else:
    print("The string is not palindrome")
