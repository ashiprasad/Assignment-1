# 18.Write a python program that checks if two strings are anagrams of each other
input1 = input("Enter the first string:")
input2 = input("Enter the second string:")
if (sorted(input1)==sorted(input2)):
    print("The strings are anagrams")
else:
    print("The string are not anagram")


