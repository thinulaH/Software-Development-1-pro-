# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID (UOW): w2051872 
# Student ID (IIT): 20231158
# Date: 2023.12.09

from graphics import *
from w2051872_histogram import *
from w2051872_input import *
from w2051872_selection import *

def main():
    want_to_continue = 'y'
    list_out = []
    print()
    while want_to_continue == 'y' :
        #input credits and validate
        prog_out,pro_count,pro_m_count,excl_count,dnp_count,cred_pass,cred_defer,cred_fail = input_credits()
        print(prog_out,'\n')

        list_in = [prog_out, cred_pass, cred_defer, cred_fail]
        if  list_in[0] == 'Do not progress - module retriever' :
            list_in[0] = 'Module retriever'
        list_out.append(list_in)
        want_to_continue = selection()
        print()

    if want_to_continue == 'q' :
        #display histogram
        histogram(pro_count,pro_m_count,dnp_count,excl_count)
        #print list
        print('Part 2:')
        for list_in in list_out :
            print(f"{list_in[0]} - {list_in[1]}, {list_in[2]}, {list_in[3]}")
        print()
if __name__ == "__main__":
    main()
