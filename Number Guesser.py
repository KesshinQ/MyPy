import random

top_range = input("Enter a number: ")

if top_range.isdigit():
    top_range = int(top_range)

    if top_range <= 0:
        print("Type a number larger than 0 next time.")
        quit()
else:
    print("Type a number next time.")
    quit()

rnd_number = random.randint(0 , top_range)
guess_count = 0
guess_left = 6

while True:

    guess_count += 1
    print("You got", guess_left , "guesses left.")

    if guess_left == 0:
        print("You failed, good luck next time :)")
        break


    user_guess = input("Make a guess: ")

    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Type a number next time.")
        continue

    if user_guess == rnd_number:
        print("You got it!")
        print("You got it in with", guess_count, "guesses.")
        break
    elif user_guess > rnd_number:
        print("You were above the number.")
    elif user_guess < rnd_number:
        print("You were below the number.")

    guess_left -= 1






