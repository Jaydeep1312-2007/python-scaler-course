#logical operators

print("List of logical operators in python" , "and", "or", "not", sep="\n")

a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))

print("Logical and of a and b is" , a > b and b > a)
print("Logical or of a and b is" , a > b or b > a)
print("Logical not of a is" , not (a > b))

print(0 or 1)