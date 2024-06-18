# 5.Write a program that takes a string input from the user and writes it to a text file

input1 = input("Enter a string to write to the file: ")
file = "output.txt"
with open(file, "w") as f:
 f.write(input1)
print("The string has been written to", file)

