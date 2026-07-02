#input Function to take input from user


name = input("Enter your name: ")
print("Hello, " + name + "!")

n=int(input("Enter a number: "))
print("You entered:", n) 
"""only interger value  can be print if user enter a float value it will give an error because we are converting the input to integer using int() function"""

f = float(input("Enter a float number: "))
print("You entered:", f)
"""only float value  can be print if user enter a string value it will give an error because we are converting the input to float using float() function"""






#type conversion

x = 5
y = float(x) #converting integer to float
print("Value of y =", y) #output: Value of y = 5.0

a = 10.5
b = int(a) #converting float to integer
print("Value of b =", b) #output: Value of b = 10

c="123.45"
d = float(c) #converting string to float
print("Value of d =", d) #output: Value of d = 123.45

e = int(d)#converting float to integer
print("Value of e =", e) #output: Value of e = 123
