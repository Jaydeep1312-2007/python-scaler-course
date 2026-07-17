book_t = ()

movies = (
    (1,"Avengers", 250),
    (2,"Pushpa 2", 200),
    (3,"Kalki", 300),
    (4,"KGF", 180)
)

while True:

    print("========== Movie Ticket Booking ==========\n1. View Movies\n2. Book Ticket\n3. Search Movie\n4. Show My Ticket\n5. Exit")
    c = int(input("Enter your choice :- "))
    
    if c == 1:
        print("Here all movies with Ticket Price:-")

        for view in movies:

            print("Movie id :",view[0],"Movie name :" , view[1] , "Price :" , view[2])

    elif c == 2:

        ch = int(input("Enter Your Movie id :- "))
        found = False

        for id in movies:
            if id[0] == ch:
                print("Ticket can be Book Successfully...")

                book_t = (id[1],id[2])
                found = True
                break
        if found == False:
                    print("Enter a valid movie id...")

    elif c == 3:

        ch = input("Enter movie name:-")
        f = False

        for id in movies:
            if ch.lower() == id[1].lower():
                    print("Movie name: " ,id[1] , "price : ",id[2])
                    f = True
                
        if f == False:
                    print("No Movies")

    elif c == 4:
        if len(book_t) == 0:
             print("No movie book")
        else:
             print("Movie name : " , book_t[0] , "Price : " , book_t[1])

    elif c == 5 :
        print("Thank you")
        break
    else:
        print("Enter valid choice")





                    


        
