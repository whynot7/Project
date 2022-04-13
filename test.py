import random
lower = 0
upper = 100
max_guesses = 10
to_guess = random.randint(lower, upper)
current_guess = -1
num_guesses = 0
while current_guess != to_guess:
    num_guesses += 1
    if num_guesses > max_guesses:
        print("Maximum number of guesses exceeded")
        break
    current_guess = int(input("Your guess (between {} and {})".format(lower, upper)))
    if current_guess < 0:
        print("Bye.")
        break
    if current_guess > to_guess:
        print("You guessed too high.")
        upper = current_guess
    elif current_guess < to_guess:
        print("You guessed too low.")
        lower = current_guess
else:
    print("You got it!")
