"""
Access a element 
"""

product = {
    'bag' : 1000,
    'bottle' : 500,
    'books' : 700
}

print(product)

#print(product[0]) // error

print(product['bag'])   # from a key we can access a value 

print(product.get("books"))

#print(product.get("Python book")) if it not present so it can give a error

#so solution is 

print(product.get('python book', "Not live now"))

"""
Update a element
"""

product['bottle'] = 250
print(product)

product['books'] = 500
print(product)

"""
Add a new key value pair
"""

product['pen box'] = 60
print(product)

"""
key : inside dict
"""

product['books'] = {
    'python book': 200,
    'Java book' : 300 
}

print(product)

"""
concat a dicts
"""

product1 = {
    'laptop' : 65000,
    'mobile' : 25000,
    'watch' : 1000
}

product.update(product1)

print(product)