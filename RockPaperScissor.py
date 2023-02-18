import random

print("=================Welcome to Rock Paper Scissor=========================")
print()
u_score = 0
c_score = 0
ties = 0
print(" USER's TURN")
print("-------------")
print()
name = input("Enter your name:")
print("""
Winning Rules:
--------------
1.Paper vs Rock ===> Paper
2.Rock  vs Scissors ===> Rock
3.Scissors vs Paper ===> Scissors""")
print()
print()
print("Choices:\n1.ROCK\n2.PAPER\n3.SCISSORS")
print()
while True:

    choice = int(input("Enter your choice from 1-3:"))
    print()
    while choice > 3 or choice < 1:
        choice = int(input("Enter valid input:"))

    if choice == 1:
        u_choice = "ROCK"
    elif choice == 2:
        u_choice = "PAPER"
    else:
        u_choice = "SCISSORS"

    print("User's Choice:", u_choice)
    print("\n")
    print(" Computer's Turn")
    print("-----------------")

    comp = random.randint(1, 3)
    if comp == 1:
        cp_choice = "ROCK"
    elif comp == 2:
        cp_choice = "PAPER"
    else:
        cp_choice = "SCISSORS"

    print("Computer's Choice:", cp_choice)

    if (u_choice == "PAPER" and cp_choice == "ROCK" or u_choice == "ROCK" and cp_choice == "PAPER"):
        print("\nPAPER WINS")
        result = "PAPER"
    elif (u_choice == "SCISSORS" and cp_choice == "ROCK" or u_choice == "ROCK" and cp_choice == "SCISSORS"):
        print("\nROCK WINS")
        result = "ROCK"
    elif (u_choice == cp_choice):
        print("\nTIES")
        result = "TIES"
    else:
        print("SCISSORS WINS")
        result = ("\nSCISSORS")

    if result == "TIES":
        print("It's a TIE")
        ties = ties+1
    elif result == u_choice:
        print("USER's WINS")
        u_score = u_score+1
    else:
        print("COMPUTER's WINS")
        c_score = c_score+1
    print()
    print(" SCORES ")
    print("---------")
    print()
    print(name, "'s score:", u_score)
    print("Computer Score:", c_score)
    print("Tie Score:", ties)
    repeat = input("Do You want to play again?")
    if repeat == "No" or repeat == "no":
        break

print("GAME OVER")
print()
print()
print("===================THANKS FOR PLAYING===================")
