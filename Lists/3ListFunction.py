"""
LIst have many function

1. count
2. index
3. pop
4. remove
5. sort
6. insert
7. append
8. extend"""

l = ["jaydeep" , 21, 45.34 , 'j' , 21,"jaydeep"]

print(":::::::::::count method is used for count how many time return :::::::::::")
print("count example :- ",l.count(21),"\n")  

print(":::::::::::index method is used for find a index in a list :::::::::::")
print("index example :- ",l.index('j'),"\n") 

print(":::::::::::pop method is used for remove a last element:::::::::::")
print("pop example :- ",l.pop(),"\n") 
print(l)

print(":::::::::::remove method is used for remove a specific element :::::::::::")
print("remove example :- ",l.remove(21),"\n",l)

l1= [3,567,245,135,556,456,2345,456,]
print(":::::::::::sort method is used for sort a list:::::::::::")
s = l1.sort()
print("sort example :- ",l1,"\n") 

print(":::::::::::insert method is used for insert a elements with specific index :::::::::::")
l.insert(1,"Hii")    #index specific compulsory otherwise error 
print("insert example :- ",l,"\n")

print(":::::::::::append method is used for insert a element in a last index of list:::::::::::")
num = [34 ,56, 78,45,76,21,45]
num.append(l1)   #[34, 56, 78, 45, 76, 21, 45, [3, 135, 245, 456, 456, 556, 567, 2345]] 
print("append example :- " ,num,"\n")

print(":::::::::::extend method is used for to insert in a last but it can divide into a elements :::::::::::")
name = "bhavy"
l.extend(name)   # ['jaydeep', 'Hii', 45.34, 'j', 21, 'b', 'h', 'a', 'v', 'y'] 
print("append example :- " ,l,"\n")