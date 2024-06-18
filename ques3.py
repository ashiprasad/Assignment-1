# Write a python program that calculates the factorial of a given number.
num = int(input("Enter a number: "))
factorial = 1
a = 1
while a<=num:
    factorial = factorial * a
    a = a + 1
print("Factorial of",num,"is",factorial)



