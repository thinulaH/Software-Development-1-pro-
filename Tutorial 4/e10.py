import random
rand_num = random.randint(1,20)
guess_count = 0
while guess_count < 5 :
    guess = int(input("Enter guess : "))
    guess_count = guess_count + 1
    if guess == rand_num :
        break
    elif guess < rand_num :
        print("Your guess is too low ")
    else:
        print("Your guess is too high ")
if guess == rand_num :
    print("You got it in",guess_count,"guesses")
else:
    print("Not guessed. The correct answer was:",rand_num)
