import random, sys 

print("ROCK, PAPER, SCISSORS")
print("0 wins, 0 lose, 0 tie")

win = 0
lose = 0
tie = 0

choice = ""

while True: 
  move = input("enter your move, (r)ock, (p)aper, (s)cissor, (q)uit: ")
  correct = int(random.randint(1, 3))

  if correct == 1:
    choice = "ROCK"
  elif correct == 2:
    choice = "PAPER"
  elif correct == 3:
    choice = "SCISSOR"

  if move == "r":
    print("ROCK VERSUS...")
    print(choice)
    if choice == "ROCK":
      print("it is a tie!")
      tie = tie + 1
      print(win, "wins", lose, "lose", tie, "tie")
      continue
    elif choice == "PAPER":
      print("you lose!")
      lose = lose + 1
      print(win, "wins", lose, "lose", tie, "tie")
      continue
    elif choice == "SCISSOR":
      print("you win!")
      win = win + 1
      print(win, "wins", lose, "lose", tie, "tie")
      continue
  
  elif move == "p":
    print("PAPER VERSUS...")
    print(choice)
    if choice == "PAPER":
      print("it is a tie!")
      tie= tie + 1
      print(win, "wins", lose, "lose", tie, "tie")
      continue
    elif choice == "ROCK":
      print("you win!")
      win = win + 1
      print(win, "wins", lose, "lose", tie, "tie")
      continue
    elif choice == "SCISSOR":
      print("you lose!")
      lose = lose + 1
      print(win, "wins", lose+1, "lose", tie, "tie")
      continue

  elif move == "s":
    print("SCISSOR VERSUS...")
    print(choice)
    if choice == "SCISSOR":
      print("it is a tie!")
      tie = tie + 1
      print(win, "wins", lose, "lose", tie, "tie")
      continue
    elif choice == "PAPER":
      print("you lose!")
      lose = lose + 1
      print(win, "wins", lose, "lose", tie, "tie")
      continue
    elif choice == "ROCK":
      print("you win!")
      win = win + 1
      print(win, "wins", lose, "lose", tie, "tie")
      continue
  elif move == "q":
    sys.exit()
