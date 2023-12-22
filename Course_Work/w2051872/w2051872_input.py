# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID (UOW): w2051872 
# Student ID (IIT): 20231158
# Date: 2023.12.09

pro_count,pro_m_count,dnp_count,excl_count = 0,0,0,0
credits = [0,20,40,60,80,100,120]

#Input value and checking the input value in range and is an integer
def validate(cred_name,credits) :
    while True:
        try:
            credit_value = int(input(f"Please enter your credits at {cred_name}: "))
            if credit_value in credits:
                return credit_value 
            else:
                print('Out of range.')
        except ValueError:
            print('Integer required')

#getting inputs for pass, defer and fail values from user and decide progress outcome
def input_credits():
    global pro_count,pro_m_count,excl_count,dnp_count
    while True :
        cred_pass  = int(validate('PASS ',credits))
        cred_defer = int(validate('DEFER',credits))
        cred_fail  = int(validate('FAIL ',credits))
        Total = cred_defer+ cred_fail+ cred_pass
        if Total == 120:
            break
        else:
            print('Total incorrect. ')
    if cred_pass == 120:
        prog_out = 'Progress'
        pro_count += 1
    elif cred_pass == 100:
        prog_out = 'Progress (module trailer)'
        pro_m_count += 1
    elif (cred_fail in [80,100,120]):
        prog_out = 'Exclude'
        excl_count += 1
    else:
        prog_out = 'Do not progress - module retriever'
        dnp_count += 1
    return prog_out,pro_count,pro_m_count,excl_count,dnp_count,cred_pass,cred_defer,cred_fail