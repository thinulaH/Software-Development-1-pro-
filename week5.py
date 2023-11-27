secret = 'hello'

guess = input('Enter guess :')
guesse = guess.lower()
guesses = " "
turn = len(secret)


while turn>0:
    missed = 0 
    guesses += guess
    for letter in secret:
        if letter in guesses:
            print(" ",letter,end = " ")
        else:
            print(" _ ",end = " ")
            missed += 1
    if guess not in secret :
        print("Incorrect")
        turn -= 1
        print(turn,"turns left")
        
            
    print("")
    guess = input("Enter guess :")
    guesses = guesses + guess
    print()
    if missed == 0:
        print("Win!")
        break
    if turn == 0:
        print("correct answer is",secret)
print("END")

    
