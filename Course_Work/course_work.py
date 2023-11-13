

want_to_continue = 'y'

while want_to_continue == 'y' :
    try:
        cred_pass  = int(input('Please enter your credits at pass : '))
        cred_defer = int(input('Please enter your credits at defer: '))
        cred_fail  = int(input('Please enter your credits at fail : '))
    except ValueError :
        print('Integer required')
        break
    if (cred_defer + cred_pass + cred_fail) != 120 :
        print('Total incorrect. ')
    
    if cred_pass == 120 :
        prog_out = 'Progress'
    if cred_pass == 100 :
        prog_out = 'Progress (module trailer)'
    if cred_pass in(80,60) :
        prog_out = 'Do not Progress - module retriever'
    if cred_pass == 40 :
        if cred_defer == 0 :
            prog_out = 'Exclude'
        else :
            prog_out = 'Do not Progress - module retriever'
    if cred_pass == 20 :
        if cred_defer in(0,20) :
            prog_out = 'Exclude'
        else :
            prog_out = 'Do not progress - module retriever'
    if cred_pass == 0 :
        if cred_defer in(60,80,100,120):
            prog_out = 'Do not progress - module retriever'
        else :
            prog_out = 'Exclude'
    print(prog_out)
    print('Would you like to enter another set of data?')
    want_to_continue = input("Enter 'y' for yes or 'q' to quit and view results: ")
if want_to_continue == 'q' :
    print("quiting ...")
    
