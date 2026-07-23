"""
3 way to delete a elements

1. pop()   #specific element to delete
2. popitem()  #delete a last element
3. del to delete whole dict
"""


#1
product = {
    'laptop' : 65000,
    'mobile' : 25000,
    'watch' : 1000
}

product.pop('laptop')
print(product)

product.pop('mobile')
print(product)


#2

product = {
    'laptop' : 65000,
    'mobile' : 25000,
    'watch' : 1000
}

product.popitem()
print(product)

product.popitem()
print(product)

#3

del product  
# print(product)   error not defined