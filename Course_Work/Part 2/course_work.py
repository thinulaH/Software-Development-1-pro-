from graphics import *

#Input value and checking the input value in range and is an integer
def input_cred(cred_name,credits) :
    while True:
        try:
            credit_value = int(input(f"Please enter your credits at {cred_name}: "))
            if credit_value in credits:
                return credit_value 
            else:
                print("Out of range.")
        except ValueError:
            print('Integer required')

#column colours
def col_colours(place) :
    if   place == 1 :
        r,g,b = 169,150,180
    elif place == 2 :
        r,g,b = 184,217,180
    elif place == 3 :
        r,g,b = 132,171,180
    elif place == 4 :
        r,g,b = 232,145,155
    return r,g,b 

#column height adjestment
def col_height(pro_count,pro_m_count,dnp_count,excl_count) :
    vals = [pro_count,pro_m_count,dnp_count,excl_count]
    n = 1
    while any(val*80/n > 400 for val in vals) :
            n += 0.2
    #https://www.programiz.com/python-programming/methods/built-in/any (any() function: works similar as 'or')
    return n
 
#making columns
def rectangle(place,height_rec) :
    r, g, b = col_colours(place)
    x1,x2 = (80+(place*110)),(175+(place*110))
    y1 = 500
    y2 = y1 - (80*(height_rec/n))
    rectangle1 = Rectangle(Point(x1,y1),Point(x2,y2))
    rectangle1.setFill(color_rgb(r,g,b))
    rectangle1.setOutline(color= "Black")
    rectangle1.setWidth(0.5)
    rectangle1.draw(Win)
    return x1,x2,y1,y2

#main title in paragraph
def title() :
    title_histo = Text(Point(220,40),"Histogram Results")
    title_histo.setSize(35)
    title_histo.setTextColor(color_rgb(103,103,103))
    title_histo.setStyle("bold")
    total_txt = Text(Point(150,570),total)
    total_txt.setTextColor(color_rgb(36,36,36))
    total_txt.setSize(25)
    total_txt.draw(Win)
    title_histo.draw(Win)

#column names
def subTitle():
    x1,x2,y1,y2 = rectangle(place,height_rec)
    x = (x1+x2)/2
    y = y1 + 20
    sub_t_histo = Text(Point(x,y),sub_title)
    sub_t_histo.setSize(20)
    sub_t_histo.setTextColor(color_rgb(120,120,120))
    num_count = Text(Point(x,y2-10),(int(height_rec)))
    num_count.setSize(18)
    num_count.setTextColor(color_rgb(150,150,150))
    sub_t_histo.draw(Win)
    num_count.draw(Win)
    
pro_count,pro_m_count,dnp_count,excl_count = 0,0,0,0
height_rec = 0 
tot_outcomes = 0
place = 1 
want_to_continue = 'y'
sub_titles = ["Progress","Trailer","Retriver","Excluded"]
credits = [0,20,40,60,80,100,120]
list_out = []
count = 0
i = 0

while want_to_continue == 'y' :
    while True :
        cred_pass  = int(input_cred('PASS ',credits))
        cred_defer = int(input_cred('DEFER',credits))
        cred_fail  = int(input_cred('FAIL ',credits))
        Total = cred_defer+cred_fail+cred_pass
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
    
    list_in = [prog_out, cred_pass, cred_defer, cred_fail]
    if list_in[0] == 'Do not progress - module retriever' :
        list_in[0] = 'Module retriever'
    list_out.append(list_in)
    count += 1
    
    print(prog_out,'\n')
    print('Would you like to enter another set of data?')
    want_to_continue = input("Enter 'y' for yes or 'q' to quit and view results: ")
    while want_to_continue not in ['y','q']:
        want_to_continue = input("Enter 'y' for yes or 'q' to quit and view results: ")   
    print()

if want_to_continue == 'q' :
    #display histogram
    Win = GraphWin("histogram", 805, 600)
    Win.setBackground(color_rgb(237,242,236))
    linex = Line(Point(150,500),Point(650,500))
    tot_outcomes = pro_count + pro_m_count + dnp_count + excl_count
    total = str(tot_outcomes)+" outcomes in total."
    title()
    #display columns
    for height_rec in (pro_count,pro_m_count,dnp_count,excl_count):
        n = col_height(pro_count,pro_m_count,dnp_count,excl_count)
        col_colours(place)
        rectangle(place,height_rec/n)
        sub_title = sub_titles[place-1]
        subTitle()
        place += 1
     
    linex.draw(Win)
    Win.getMouse()
    Win.close()
    #print list
    print('Part 2:')
    while i<count :
        print(f"{list_out[i][0]} - {list_out[i][1]}, {list_out[i][2]}, {list_out[i][3]}")
        i += 1
    print()
