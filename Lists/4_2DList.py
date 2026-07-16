l1 = [1,2,3]
l2 = [4,5,6]
l3 = [7,8,9]

l= [l1,l2,l3]
print(l)

print(l[0] , "\n" , l[1] , "\n" , l[2])

"""
 [1, 2, 3] 
 [4, 5, 6] 
 [7, 8, 9]    """

print(l[1][2]) #6

print(l[1][0]) #4



"""Iteration on 2D list"""

for i in l:
    print(i)
"""
 [1, 2, 3] 
 [4, 5, 6] 
 [7, 8, 9]    """

for i in l:
    for j in i:
        print(j , end=" ") #1 2 3 4 5 6 7 8 9 




