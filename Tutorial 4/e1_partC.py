import random

hidden_val = str(random.randint(1,20))
guess = input("Enter guess value : ")

while guess != hidden_val :
    print(guess,"is not correct")
    if guess < hidden_val:
        print("too low ... ")
    elif guess > hidden_val :
        print("too high ... ")
    guess = input("Enter guess value : ")
print(guess, "was correct")
    

