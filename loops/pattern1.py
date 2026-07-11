"""first pattern using for loop is 
*
**
***
****
*****"""

n = int(input("Enter a number :-"))

a = 0
b=1

for i in range(1,n+1):
    for j in range(i):
        print(i , end =" ")
    print()
"""
1 
2 2 
3 3 3
"""

for i in range(1,n+1):
    for j in range(i):
        print(j , end =" ")
    print()

"""
0 
0 1 
0 1 2 
"""
for i in range (1,n+1):
    for j in range(i):
        print(  a+i , end = " ")
        a+=1
    print()

"""
1 
3 4 
6 7 8 
"""

for i in range (1,n+1):
    for j in range(i):
        print(  chr(96 +i) , end = " ")
        
    print()

"""
a 
b b 
c c c 
"""

for i in range (1,n+1):
    for j in range(i):
        print(  chr(97 +j) , end = " ")
        
    print()

"""
a 
a b 
a b c 
"""
for i in range (1,n+1):
    for j in range(i):
        print(  chr(96 +b) , end = " ")
        b+=1
    print()

"""
a 
b c 
d e f 
"""

