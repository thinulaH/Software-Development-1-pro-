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
    print()
    user = selection("Select user type\nEnter 's' for student or 't' for teacher: ","Invalid user type!\nEnter 's' for student or 't' for teacher: ",'s','t')
    if user == 's' :
        #input credits
        prog_out,pro_count,pro_m_count,excl_count,dnp_count = input_credits()[0:5]
        print(prog_out,'\n')
    elif user == 't':
        while want_to_continue == 'y' :
            #input credits
            prog_out,pro_count,pro_m_count,excl_count,dnp_count = input_credits()[0:5]
            print(prog_out,'\n')
            want_to_continue = selection("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: ","Enter 'y' for yes or 'q' to quit and view results: ",'y','q')
            print()
        if want_to_continue == 'q' :
            #display histogram
            histogram(pro_count,pro_m_count,dnp_count,excl_count)

if __name__ == "__main__":
    main()