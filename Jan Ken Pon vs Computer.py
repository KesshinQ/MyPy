import random

user_wins = 0
computer_wins = 0

options = ["rock" , "paper" , "scissors"]

while True:
    user_inp = input("Type Rock/Paper/Scissors to play or type Q to quit. ").lower()

    if user_inp == "q":
        break

    if user_inp not in options:
        print("Please type rock, paper or scissors to play. ")
        continue

    rnd_num = random.randint(0,2)

    comp_pick = options[rnd_num]
    print("Computer picked " , comp_pick , ".")

    if user_inp == "rock" and comp_pick == "scissors":
        print("You won!")
        user_wins += 1

    elif user_inp == "paper" and comp_pick == "rock":
        print("You won!")
        user_wins += 1

    elif user_inp == "scissors" and comp_pick == "paper":
        print("You won!")
        user_wins += 1

    elif user_inp == comp_pick:
        print("Draw! Again!")

    else:
        print("Computer won!")
        computer_wins += 1

print("You won " , user_wins , "times.")
print("The computer won " , computer_wins , "times.")
print("See you next time :)")
