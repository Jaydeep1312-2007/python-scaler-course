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

#only print values

print("Only values")
for i in product:
    print(product[i])

# Both print with a simple methods

print("Key    value pair")
for i in product:
    print(i,product[i])

#using a items() function

print("key and value Using a items() method")

for key,value in product.items():
    print(key,"->",value)