import random

print("=====================================")
print("      🎯 GUESS THE NUMBER GAME      ")
print("=====================================")
while True:
  print(" 1.Easy(1-10) \n 2.(1-100) \n 3.(1-1000)")
  a = int(input("Choose a Level for a game:-  "))

  if a == 1:
    print("Guess a Number Between 1 to 10 with a 3 attempt........")
    n = random.randint(1,10)
    attempt = 3

    for i in range(1,5):
      if attempt == 0:
            print("You lose the game❌")
            print("Number is :- ",n)
            break
      else:
              guess = int(input("Enter your guess Number:- "))
              attempt -= 1
              if guess == n:
                print("🎉 Congratulations!")
                print("Remaining Attempt only ⏳ ",attempt)
                print("Thanks for playing")
                break
              elif guess< n:
                print("Too low⬇️")
                print("Remaining Attempt only ⏳ ",attempt)
              elif guess> n:
                print("Too High⬆️")
                print("Remaining Attempt only ⏳ ",attempt)
              else:
                  print("Enter a vaild Guess")

  elif a == 2:
    print("Guess a Number Between 1 to 100 with a 10 attempt........")
    n = random.randint(1,100)
    attempt = 12

    for i in range(1,14):
      if attempt == 0:
            print("You lose the game❌")
            print("Number is :- ",n)
            break
      else:
              guess = int(input("Enter your guess Number:- "))
              attempt -= 1
              if guess == n:
                print("🎉 Congratulations!")
                print("Remaining Attempt only ⏳ ",attempt)
                print("Thanks for playing")
                break
              elif guess< n:
                print("Too low⬇️")
                print("Remaining Attempt only ⏳ ",attempt)
              elif guess> n:
                print("Too High⬆️")
                print("Remaining Attempt only ⏳ ",attempt)
              else:
                  print("Enter a vaild Guess")

  elif a == 3:
    print("Guess a Number Between 1 to 1000 with a 15 attempt........")
    n = random.randint(1,1000)
    attempt = 15

    for i in range(1,17):
      if attempt == 0:
            print("You lose the game❌")
            print("Number is :- ",n)
            break
      else:
              guess = int(input("Enter your guess Number:- "))
              attempt -= 1
              if guess == n:
                print("🎉 Congratulations!")
                print("Remaining Attempt only ⏳ ",attempt)
                print("Thanks for playing")
                break
              elif guess< n:
                print("Too low⬇️")
                print("Remaining Attempt only ⏳ ",attempt)
              elif guess> n:
                print("Too High⬆️")
                print("Remaining Attempt only ⏳ ",attempt)
              else:
                  print("Enter a vaild Guess")

  else:
    print("plz Enter correct choose")

  play = input("\nDo you want to play again? (y/n): ").lower()

  if play == "y":
    continue
  elif play == "n":
    print("Thanks for playing! 😊")
    break
  else:
    print("Invalid input. Exiting the game.")
    break
            
            
