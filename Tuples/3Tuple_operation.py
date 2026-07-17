T1 = (1,2,3,4 , "Jaydeep" , 3,6.7,1,'f')

# count

print(T1.count(3))

print(T1.count('f'))


#Index

print(T1.index(2))

print(T1.index("Jaydeep"))

#Ieration 

print(len(T1))

for i in T1:
    print(i , end = " ")

#concatination

t2 = (10, 'r' , "Darji")

t3 = T1+t2
print("\n" , t3)

t4 = t3*2
print(t4)

#list to tuple and tuple to list

L1 = list(T1)
print(L1)

L2 = [3,4,5,6,7,8,9]

T6 = tuple(L2)

print(T6)