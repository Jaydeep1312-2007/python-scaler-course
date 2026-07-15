"""Palindrome means 

string == reverse string

example naman == naman """

s1 = input("Enter a string :- ")

s2 = s1[::-1]

if s1 == s2:
    print("Palindrome")
else:
    print("Not Palindrome")