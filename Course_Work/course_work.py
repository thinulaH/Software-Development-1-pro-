from graphics import *

want_to_continue = 'y'

def rectangle() :
    rectangle1 = Rectangle(Point((80+(place*100)),500),Point(150+(place*100),(500-(80*height_rec))))
    rectangle1.setFill(color_rgb(107,100,120))
    rectangle1.setOutline(color="Black")
    rectangle1.setWidth(3)
    rectangle1.draw(Win)

def title() :
    title_histo = Text(Point(220,40),"Histogram Results")
    title_histo.setSize(35)
    title_histo.setTextColor(color_rgb(103,103,103))
    title_histo.setStyle("bold")
    title_histo.draw(Win)

pro_count = 0
#pro_count = progress count
dnp_count = 0
#dnp_count = do not progress - module retriver count
pro_m_count = 0
#pro_m_count = progress (module trailer)
excl_count = 0
#excl_count = exclude count
height_rec = 0 
col_num = 0
place = 1 

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
        pro_count = pro_count + 1
    elif cred_pass == 100 :
        prog_out = 'Progress (module trailer)'
        pro_m_count = pro_m_count + 1
    elif cred_pass in(80,60) :
        prog_out = 'Do not Progress - module retriever'
        dnp_count = dnp_count + 1 
    elif cred_pass == 40 :
        if cred_defer == 0 :
            prog_out = 'Exclude'
            excl_count = excl_count + 1
        else :
            prog_out = 'Do not Progress - module retriever'
            dnp_count = dnp_count + 1
    elif cred_pass == 20 :
        if cred_defer in(0,20) :
            prog_out = 'Exclude'
            excl_count = excl_count + 1
        else :
            prog_out = 'Do not progress - module retriever'
            dnp_count = dnp_count + 1
    elif cred_pass == 0 :
        if cred_defer in(60,80,100,120):
            prog_out = 'Do not progress - module retriever'
            dnp_count = dnp_count + 1
        else :
            prog_out = 'Exclude'
            excl_count = excl_count + 1
    print(prog_out)
    print('Would you like to enter another set of data?')
    want_to_continue = input("Enter 'y' for yes or 'q' to quit and view results: ")
if want_to_continue == 'q' :
    print("quiting ...")
    Win = GraphWin("histogram", 800, 600)
    Win.setBackground(color_rgb(237,242,236))
    linex = Line(Point(80,500),Point(720,500))
    title()
    for col_num in (pro_count,pro_m_count,excl_count,dnp_count) :
        height_rec = col_num
        print(height_rec)
        rectangle()
        place = place + 1
    linex.draw(Win)
    Win.getMouse()
    Win.close()



    

