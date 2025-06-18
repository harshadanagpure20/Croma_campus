#Given two Boolean variables a and b, write a program to evaluate and print the result of a
#and b, a or b, and not a.
a = bool(input("Enter the value for a : "))
b = bool(input("Enter the value for b : "))
result_of_a_and_b = a and b
result_of_a_or_b = a or b
result_of_not_a = not a
print("Result of a and b",result_of_a_and_b)
print("Result of a or b ",result_of_a_or_b)
print("Result of not a ",result_of_not_a)
