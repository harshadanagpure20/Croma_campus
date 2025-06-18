#Write a program to check if a number exists in a given list.
#Write a program that checks if a keyword like "data" isin a list of strings.
list = [1,2,3,4,56,78,90,7,'data','Harshada']
num = input("Enter the number you want to check : ")
if num in list:
    print("Present")
else:
    print("Not Present")