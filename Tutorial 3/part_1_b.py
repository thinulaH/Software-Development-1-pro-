##b

try :
    age= int(input("How old are you? : "))
    if age >= 18:
        print("Can vote")
except :
    print('Value Error , please enter an integer')
