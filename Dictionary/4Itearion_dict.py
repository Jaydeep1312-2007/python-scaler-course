product = {
    'laptop' : 65000,
    'mobile' : 25000,
    'watch' : 1000,
    'books' : 500
}

print(product)


# only print keys

print("Only keys")
for i in product:
    print(i)

print("key using a keys() function")
for i in product.keys():
    print(i)


#only print values

print("Only values")
for i in product:
    print(product[i])

print("Value using a values() function")

for i in product.values():
    print(i)

# Both print with a simple methods

print("Key    value pair")
for i in product:
    print(i,product[i])

#using a items() function

print("key and value Using a items() method")

for key,value in product.items():
    print(key,"->",value)