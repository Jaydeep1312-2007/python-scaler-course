s = []

while True:
    print("========== Student Management System ==========\n1. Add Student\n2. View Students\n3. Search Student\n4. Update Student\n5. Delete Student\n6. Sort Students\n7. Total Students\n8. Exit")
    c = int(input("Enter a choice:- "))

    if c == 1:

        while True:
            e = int(input("Enter a Enrollment Number :- "))
            n = input("Enter a Student Name :- ")
            m = int(input("Enter a mark :- "))
            s1 = [e,n,m] 
            s.append(s1)

            c1 = input("Do you add another student (y/n)")
            if c1 == 'y':
                continue
            else:
                print("Thank you..")
                break
    
    elif c == 2:

        if len(s)== 0:
            print("NO record of student")
        else:

            print("=========== Student list ==========")
            for student in s:
                print("Enrollment no : " ,  student[0] , ", Name :- " , student[1] , ", Mark :- " , student[2])

    elif c == 3:

        ser = input("Enter student name :- ")
        found = False

        for student in s:
            if student[1].lower() == ser.lower():
                print("========== Student Found ==========")
                print("Enrollment no : " ,  student[0] , ", Name :- " , student[1] , ", Mark :- " , student[2])
                found = True
                break
        if found == False:
                print("No Student Found!")

    elif c == 4:
        ser = input("Enter student name :- ")
        found = False

        for student in s:
            if student[1].lower() == ser.lower():
                print("Enrollment no : " ,  student[0] , ", Name :- " , student[1] , ", Mark :- " , student[2])
                up = int(input("Enter 1-Enrollment 2-Name 3-Marks : "))

                if up == 1:
                    ee= int(input("Enter a new enrollment No. :- "))
                    student[0] = ee
                elif up == 2:
                    nn= input("Enter a new Namne :- ")
                    student[1] = nn
                elif up == 3:
                    mm= int(input("Enter a new Marks :- "))
                    student[2] = mm
                found = True
                print("Student Updated Successfully!")
                print("Enrollment no : " ,  student[0] , ", Name :- " , student[1] , ", Mark :- " , student[2])
                break
        if found == False:
                print("No Student Found!")

    elif c == 5:
        ser = input("Enter student name :- ")
        found = False

        for student in s:
            if student[1].lower() == ser.lower():
                print("========== Student Found ==========")
                print("Enrollment no : " ,  student[0] , ", Name :- " , student[1] , ", Mark :- " , student[2])
                s.remove(student)
                print("Student Deleted Successfully!")
                found = True
                break
        if found == False:
                print("No Student Found!")
    
    elif c == 6:
         s.sort()
         
         for student in s :
              print("Enrollment no : " ,  student[0] , ", Name :- " , student[1] , ", Mark :- " , student[2])
    
    elif c == 7:
        t = len(s)
        print("Total Students are :- " , t)
    
    elif c == 8:
         print("Thank you....")
         break
    else:
         print("Enter a valid Choice...")
         continue
