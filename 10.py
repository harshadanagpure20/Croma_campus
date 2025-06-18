#Write a Python program to check if a character is present in a string.
string = str(input("Enter a string: "))
char =(input("Enter a character to check: "))
if char in string:
    print("Char is present in the string")
else:
    print("Char is not present in the string")