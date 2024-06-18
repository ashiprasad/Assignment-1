# 16.Write a program in python that counts the frequency of each character in a string.
n=input("Enter the String: ").lower()
s={}
for i in n:
    if i in s:
        s[i]+=1
    else:
        s[i]=1
print(s)
