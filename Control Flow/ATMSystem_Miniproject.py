"""This is system for a ATM Machine Basic using a if elif and else"""
Total_balance = 0
while True:
    print("Welcome SBI ATM")
    print(" 1. Check Balance \n 2. Deposite \n 3. Withdraw \n 4. Exit")

    ch = int(input("Enter a your choice: - "))
    
    if ch ==1:
        print("This is your Bank balance :- " , Total_balance)
    elif ch ==2:
        amount = int(input("Enter your deposite amount:- "))
        Total_balance+=amount
        print("Successfully Deposite your amonut ")
        ch1 = int(input("Press 1 to see bank balance :- "))
        if ch1==1:
            print("This is your Bank balance :- " , Total_balance)
        else: 
            break
    elif ch ==3:
        amount = int(input("Enter your amount :- "))
        if amount<=Total_balance:
            print("Please collect your cash...")
            Total_balance-=amount
        else:
            print("Insufficient balance...") 
    elif ch==4:
        break
    else:
        print("Enter valid choice...")
    