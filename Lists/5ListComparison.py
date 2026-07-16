"""in this we can create a list with using a loop"""

for i in range(10):
    print(i)

l=[]
for i in range(10):
    l.append(i)

print(l)

l1 = []
for i in range(10):
    l1.append(i**2)

print(l1)

#Short method

l3 = [i for i in range(20)]
print(l3)

l4 = [i**2 for i in range(10)]
print(l4)