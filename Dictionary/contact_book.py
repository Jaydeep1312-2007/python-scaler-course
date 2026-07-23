contact = {}
while True:



    print("========== Contact Book ==========\n1. Add Contact\n2. View Contacts\n3. Search Contact\n4. Update Contact\n5. Delete Contact\n6. Total Contacts\n7. Exit")

    ch = int(input("Enter Your Choice:- "))

    if ch == 1:
        name = input("Enter a Name :- ")
        number = int(input("Enter a number :- "))

        if name in contact:
            print("Contact already exists!")
        else:

            num = str(number)

            if len(num) == 10:
                num = int(num)
                contact[name] = num
                print("Contact Saved Successfully")
            else:
                print("Enter a Valid number....")

    elif ch == 2:

        if len(contact)==0:
            print("No Contact Found!")

        else:
            print("Name              Number \n-----------------------------")
            for i in contact:
                print(f"{i:<15} {contact[i]}")

    elif ch == 3:

        found = False

        n = input("Enter a name :- ")

        for i in contact:
            if n.lower() == i.lower():
                print("Name              Number \n-----------------------------")
                print(f"{i:<15} {contact[i]}")
                found = True
                break
        if found == False:
                print("No Contact Found!")

    elif ch == 4:
        found = False

        n = input("Enter a name :- ")

        for i in contact:
            if n.lower() == i.lower():
                print("Enter a Name and number for update")
                name = input("Enter a Name :- ")
                number = int(input("Enter a number :- "))

                contact.pop(i)

                num = str(number)

                if len(num) == 10:
                    i = name 
                    contact[i] = num
                    print("Contact update Successfully")
                else:
                    print("Enter a Valid number....")

                print("Name              Number \n-----------------------------")
                print(f"{i:<15} {contact[i]}")
                found = True
                break
        if found == False:
                print("No Contact Found!")

    elif ch == 5:
        found = False

        n = input("Enter a name :- ")

        for i in contact:
            if n.lower() == i.lower():
                contact.pop(i)
                print("Delete contact succeefully")
                found = True
                break
        if found == False:
                print("No Contact Found!")

    elif ch == 6:
         print("Total number of contact :- " , len(contact))

    elif ch == 7:
         print("Thank you..")
         break
    else:
         print("Enter a valid choice")