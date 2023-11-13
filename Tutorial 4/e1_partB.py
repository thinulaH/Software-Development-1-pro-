import random

hidden_val = str(random.randint(1,20))
guess = input("Enter guess value : ")
print(hidden_val)
while guess != hidden_val :
    print(guess,"is not correct")
    guess = input("Enter guess value : ")
print(guess, "was correct")
    

