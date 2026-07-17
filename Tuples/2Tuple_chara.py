"""
immutable and unpacking in tuple
"""

T1 = (2,3,4,6,7,8,9)

# T1[1] = 10 so it can error because we cannot change a value of tuple

#2. unpacking

t = (10,20,30)

a,b,c = t

print(a,b,c)

# unpacking means a assigning tuple elements to multiple variables in a single line