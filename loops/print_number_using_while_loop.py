"""Now a print a number using while loop"""

i =1
while i<=10:
    print(i , end=" ")
    i+=1


"""Now a print odd and even number using while loop"""

i =0
while i<=10:

    if i%2==0:
        print(i,"is even")
    else:
        print(i,"is odd")
    
    i+=1

"""Sum of all numbers from 1 to 10"""

i=1
sum = 0

while i<=10:

    sum +=i
    i+=1

print("Sum of all number from 1 to 10 is :-" , sum)