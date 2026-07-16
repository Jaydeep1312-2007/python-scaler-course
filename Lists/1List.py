"""
List is things to stores a data with any datatype 
List is mutuable means we can change thier data
"""

l = list()
print(type(l))

#Creating a List

l1 = [1,2,3,4,5,6,7,8]
print(l1)
print(type(l1))
print(len(l1))

#Access a list like a string 

print(l1[4])
print(l1[-1])

#change a value 

l1[3] = 10
print(l1)

l1[7] = 7
print(l1)

#print a all things line by line it called itration

for i in l1:
    print(i)
