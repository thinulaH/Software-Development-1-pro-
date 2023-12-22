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
    txt_file = open("progression_data.txt","w")
    want_to_continue = 'y'

    print()
    while want_to_continue == 'y' :
        #input credits and validate
        prog_out,pro_count,pro_m_count,excl_count,dnp_count,cred_pass,cred_defer,cred_fail = input_credits()
        print(prog_out,'\n')

        if prog_out == 'Do not progress - module retriever':
            prog_out = 'Module retriever'
        txt_file.write(f"{prog_out} - {cred_pass}, {cred_defer}, {cred_fail}\n")

        want_to_continue = selection()
        print()

    if want_to_continue == 'q' :
        txt_file.close()
        #display histogram
        histogram(pro_count,pro_m_count,dnp_count,excl_count)
        #print text file
        txt_file_read = open("progression_data.txt","r")
        data = txt_file_read.read()
        txt_file_read.close()
        print('Part 3:')
        print(data)

if __name__ == "__main__":
    main()
