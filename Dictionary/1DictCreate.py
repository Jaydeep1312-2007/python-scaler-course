"""

Dictionary have a key and value 
and it cannot support a indexing """

product = {}   #empty dictionary

product = {
    'bag' : 1000,
    'bottle' : 500,
    'books' : 700
}

print(type(product))
print(product)

#zip function

p1 = ['python book' , 'c++ book' , 'Java book']
p2 = [200,150,300]

product1 = dict(zip(p1,p2))

print(product1)