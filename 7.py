#Write a program to check if a given number is divisible by 3 or 5.
num = float(input("Enter the Number : "))
if num%3==0 or num%5==0:
    print("Divisible")
else:
    print("Not Divisible")