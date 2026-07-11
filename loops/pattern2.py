"""first pattern using for loop is 
****
****
****
****"""

n = int(input("Enter a number :-"))

a = 0
b=1

for i in range(n):
    for j in range(n):
        print(i , end =" ")
    print()
"""
0 0 0 
1 1 1 
2 2 2 
"""

for i in range(n):
    for j in range(n):
        print(j , end =" ")
    print()

"""
0 1 2 
0 1 2 
0 1 2 
"""
for i in range (n):
    for j in range(n):
        print(  a+i , end = " ")
        a+=1
    print()

"""
0 1 2 
4 5 6 
8 9 10 
"""

for i in range (n):
    for j in range(n):
        print(  chr(97 +i) , end = " ")
        
    print()

"""
a a a 
b b b 
c c c 
"""

for i in range (n):
    for j in range(n):
        print(  chr(97 +j) , end = " ")
        
    print()

"""
a b c 
a b c 
a b c 
"""
for i in range (n):
    for j in range(n):
        print(  chr(96 +b) , end = " ")
        b+=1
    print()

"""
a b c 
d e f 
g h i 
"""