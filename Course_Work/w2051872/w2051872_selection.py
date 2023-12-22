# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID (UOW): w2051872 
# Student ID (IIT): 20231158
# Date: 2023.12.09

#can use when have to prompt user for two selections 
def selection():
    selection = input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: ")
    while selection not in ('y','q'):
        selection = input("Enter 'y' for yes or 'q' to quit and view results: ")
    return selection

