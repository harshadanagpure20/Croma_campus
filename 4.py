#Write a program to swap two numbers without using a third variable.
num_one = int(input("Enter the First Number :"))
num_two = int(input("Enter the second Number :"))
num_one =  num_one + num_two
num_two = num_one - num_two
num_one = num_one - num_two
print(num_one)
print(num_two)
