from graphics import *

want_to_continue = 'y'


def graph_col_text(place) :
    if place == 1:
        sub_title = "Progresss"
        r,g,b = "169","150","180"
    elif place == 2:
        sub_title = "Trailer"
        r,g,b = "184","217","180"
    elif place == 3 :
        sub_title = "Retriver"
        r,g,b = '132','171','180'
    elif place == 4 :
        sub_title = "Excluded"
        r,g,b, = "232","145","155"
    return r, g ,b 

    

def rectangle(place,height_rec) :
    r, g, b = graph_col_text(place)
    x1,x2 = (80+(place*110)), (175+(place*110))
    y1 = 500
    y2 = y1 - (80*height_rec)
    rectangle1 = Rectangle(Point(x1,y1),Point(x2,(y2)))
    rectangle1.setFill(color_rgb(int(r),int(g),int(b)))
    rectangle1.setOutline(color= "Black" )
    rectangle1.setWidth(1)
    rectangle1.draw(Win)
    return x1 , x2 ,y1


def title() :
    title_histo = Text(Point(220,40),"Histogram Results")
    title_histo.setSize(35)
    title_histo.setTextColor(color_rgb(103,103,103))
    title_histo.setStyle("bold")
    title_histo.draw(Win)

def subTitle():
    x1, x2 , y1 = rectangle(place,height_rec)
    x = (x1+x2)/2
    y = y1 + 20
    sub_t_histo = Text(Point(x,y),sub_title)
    sub_t_histo.setSize(15)
    sub_t_histo.draw(Win)



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
    Win = GraphWin("histogram", 805, 600)
    Win.setBackground(color_rgb(237,242,236))
    linex = Line(Point(150,500),Point(650,500))
    title()
    for height_rec in (pro_count,pro_m_count,dnp_count,excl_count) :
        graph_col_text(place)
        sub_title = sub_titles[place-1]
        rectangle(place,height_rec)
        subTitle()
        place = place + 1
    

    tot_outcomes = pro_count + pro_m_count + dnp_count + excl_count
    
    linex.draw(Win)
    Win.getMouse()
    Win.close()


    

