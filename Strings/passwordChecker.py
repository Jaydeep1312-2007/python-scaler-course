while True:

    p1 = input(("Enter your password:- "))

    p = p1.strip(" ")

    upper = False
    lower = False
    digit = False
    special = False
    
    for i in p:
        if i.isupper():
            upper = True
        if i.islower():
            lower = True
        if i.isdigit():
            digit=True
        if not i.isalnum():
            special = True
    if len(p) >= 8 and upper and lower and digit and special:
        print("✅ Strong Password")

    
    else:
        print("❌ Weak Password")