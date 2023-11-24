from graphics import *

#Input value and checking wether in range or adding an integer
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
    if place == 1:
        r,g,b = "169","150","180"
    elif place == 2:
        r,g,b = "184","217","180"
    elif place == 3 :
        r,g,b = '132','171','180'
    elif place == 4 :
        r,g,b, = "232","145","155"
    return r, g ,b 

#column height adjestment
def col_height(pro_count,pro_m_count,dnp_count,excl_count) :
    if pro_count >15 or pro_m_count >15 or dnp_count >15 or excl_count >15 :
        n = 5
    elif (16 > pro_count > 10) or (16 > pro_m_count > 10) or (16 > dnp_count > 10) or (16 > excl_count > 10) :
        n = 4
    elif (11 > pro_count > 5) or (11 > pro_m_count > 5) or (11 > dnp_count > 5) or (11 > excl_count > 5) :
        n = 2
    elif pro_count < 3 and pro_m_count < 3 and dnp_count < 3 and excl_count < 3 :
        n = 1/2
    else :
        n = 1
    pro_count1 = pro_count/(n)
    pro_m_count1 = pro_m_count/(n)
    dnp_count1 = dnp_count/(n)
    return pro_count1,pro_m_count1,dnp_count1,n
 
#making columns
def rectangle(place,height_rec) :
    r, g, b = col_colours(place)
    x1,x2 = (80+(place*110)), (175+(place*110))
    y1 = 500
    y2 = y1 - (80*(height_rec))
    rectangle1 = Rectangle(Point(x1,y1),Point(x2,y2))
    rectangle1.setFill(color_rgb(int(r),int(g),int(b)))
    rectangle1.setOutline(color= "Black" )
    rectangle1.setWidth(1)
    rectangle1.draw(Win)
    return x1 , x2 ,y1 

#main title in paragraph
def title() :
    title_histo = Text(Point(220,40),"Histogram Results")
    title_histo.setSize(35)
    title_histo.setTextColor(color_rgb(103,103,103))
    title_histo.setStyle("bold")
    title_histo.draw(Win)
    total_txt = Text(Point(150,570),total)
    total_txt.setTextColor(color_rgb(36,36,36))
    total_txt.setSize(25)
    total_txt.draw(Win)

#column names
def subTitle():
    x1, x2 , y1 = rectangle(place,height_rec)
    x = (x1+x2)/2
    y2 = y1 - (80*(height_rec))
    y = y1 + 20
    sub_t_histo = Text(Point(x,y),sub_title)
    sub_t_histo.setSize(20)
    sub_t_histo.setTextColor(color_rgb(120,120,120))
    sub_t_histo.draw(Win)
    num_count = Text(Point(x,y2-10),(int(height_rec*n)))
    num_count.setSize(18)
    num_count.setTextColor(color_rgb(150,150,150))
    num_count.draw(Win)

pro_count = 0
#pro_count = progress count
dnp_count = 0
#dnp_count = do not progress - module retriver count
pro_m_count = 0
#pro_m_count = progress (module trailer)
excl_count = 0
#excl_count = exclude count
height_rec = 0 
tot_outcomes = 0
#tot_outcomes = total outcomes
place = 1 
sub_titles = ["Progress","Trailer","Retriver","Excluded"]
want_to_continue = 'y'
credits = [0,20,40,60,80,100,120]

while want_to_continue == 'y' :
    while True :
        cred_pass  = int(input_cred('PASS ',credits))
        cred_defer = int(input_cred('DEFER',credits))
        cred_fail  = int(input_cred('FAIL ',credits))
        Total = cred_defer+cred_fail+cred_pass
        if Total == 120:
            break
        else:
            while Total != 120:
                print('Total incorrect. ')
                change = input("Do you want to change one credit (Enter 'c') or all credits (Enter 'a') ?  ")
                if change == 'a':
                    cred_pass  = int(input_cred('PASS ',credits))
                    cred_defer = int(input_cred('DEFER',credits))
                    cred_fail  = int(input_cred('FAIL ',credits))

                elif change == 'c':
                    print("For change \n    PASS credits  - 'p'\n    DEFER credits - 'd'\n    FAIL credits  - 'f' ")
                    change_cred = input("What input do you want to change ? :")
                    if change_cred == 'p':
                        cred_pass  = int(input_cred('PASS ',credits))
                    elif change_cred == 'd':
                        cred_defer = cred_defer = int(input_cred('DEFER',credits))
                    elif change_cred == 'f':
                        cred_fail  = int(input_cred('FAIL ',credits))
                Total = cred_defer+cred_fail+cred_pass
                if Total == 120:
                    break
            break

    if cred_pass == 120:
        prog_out = 'Progress'
        pro_count += 1
    if cred_pass == 100:
        prog_out = 'Progress (module trailer)'
        pro_m_count += 1
    if (cred_pass in [80,60]) or (cred_pass==40 and (cred_defer in [80,60,40,20])) or (cred_pass ==20 and cred_defer in[100,80,60,40]) or (cred_pass == 0 and cred_defer in [120,100,80,60]):
        prog_out = 'Do not progress - module retriever'
        dnp_count += 1
    if (cred_fail in [80,100,120]):
        prog_out = 'Exclude'
        excl_count += 1

    print(prog_out)
    print()
    print('Would you like to enter another set of data?')
    want_to_continue = input("Enter 'y' for yes or 'q' to quit and view results: ")
    while want_to_continue not in ['y','q']:
        want_to_continue = input("Enter 'y' for yes or 'q' to quit and view results: ")   
    print()

if want_to_continue == 'q' :
    Win = GraphWin("histogram", 805, 600)
    Win.setBackground(color_rgb(237,242,236))
    linex = Line(Point(150,500),Point(650,500))
    tot_outcomes = pro_count + pro_m_count + dnp_count + excl_count
    total = str(tot_outcomes)+" outcomes in total."
    title()
    col_height(pro_count,pro_m_count,dnp_count,excl_count)
    pro_count1,pro_m_count1,dnp_count1,n= col_height(pro_count,pro_m_count,dnp_count,excl_count)
    excl_count1 = (excl_count)/n

    for height_rec in (pro_count1,pro_m_count1,dnp_count1,excl_count1) :
        col_colours(place)
        rectangle(place,height_rec)
        sub_title = sub_titles[place-1]
        subTitle()
        place += 1
     
    linex.draw(Win)
    Win.getMouse()
    Win.close()



