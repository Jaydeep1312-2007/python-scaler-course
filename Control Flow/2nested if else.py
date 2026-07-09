#nested if else

age= int(input("Enter Your Age:- "))

if age<150:
   
    if age>18:

        if age>=65:
            print("Take Rest....")
        else:
            print("Your are eligible....")

    else:
        print("Your are not eligible....")
else:
    print("Enter correct age.....")
