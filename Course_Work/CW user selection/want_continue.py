def want_continue():
    print('Would you like to enter another set of data?')
    want_to_continue = input("Enter 'y' for yes or 'q' to quit and view results: ")
    while want_to_continue not in ('y','q'):
        want_to_continue = input("Enter 'y' for yes or 'q' to quit and view results: ")
    return want_to_continue