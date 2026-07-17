"""

Tuple is a dataset like a list
but tuple format is () and also tuple is immuutable so we cannot change a data

"""

T = ("Jaydeep" , 23 , 56.45 , False)
print(type(T))
print(T)

#Indexing a tuple

print(T[3])

print("Hi \n My name is" , T[0] , ".My age" , T[1])

#sciling a Tuple

print(T[0:2])
print(T[::-1])

#empty tuple 

T1= ()
print(type(T1))

#list inside a tuple

T2 = ([2,3,4] , [5,6,7])
print(type(T2))
print(T2)
print(T2[1])