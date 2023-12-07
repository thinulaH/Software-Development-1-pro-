from graphics import *
from histogram import *
from input_and_validate import *
from want_continue import *

def main():
    want_to_continue = 'y'

    print()
    while want_to_continue == 'y' :
        #input credits and validate
        prog_out,pro_count,pro_m_count,excl_count,dnp_count,cred_pass,cred_defer,cred_fail = input_credits()
        print(prog_out,'\n')
        want_to_continue = want_continue()
        print()

    if want_to_continue == 'q' :
        #display histogram
        histogram(pro_count,pro_m_count,dnp_count,excl_count)

if __name__ == "__main__":
    main()
