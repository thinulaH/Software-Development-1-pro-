credits = [0,20,40,60,80,100,120]

cred_names = [cred_pass,cred_defer,cred_fail]
cred_pass,cred_defer,cred_fail= 0,0,0
def get_input(cred_names,credits):
    cred_name  = int(input('Please enter your credits at pass : '))
    while cred_name not in credits:
        print('Out of range')
        cred_name = int(input('Please enter your credits at pass : '))
    return cred_name

        

for cred_name in cred_names:
    get_input(cred_names,credits)
    print(cred_name)
    print(cred_pass)
    
