# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID (UOW): w2051872 
# Student ID (IIT): 20231158
# Date: 2023.12.09

from graphics import *

place = 1 
sub_titles = ('Progress','Trailer','Retriver','Excluded')

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
def rectangle(n,place,height_rec,Win) :
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
def title(Win) :
    total = str(tot_outcomes)+' outcomes in total.'
    title_histo = Text(Point(220,40),'Histogram Results')
    title_histo.setSize(35)
    title_histo.setTextColor(color_rgb(103,103,103))
    title_histo.setStyle("bold")
    total_txt = Text(Point(150,570),total)
    total_txt.setTextColor(color_rgb(36,36,36))
    total_txt.setSize(25)
    total_txt.draw(Win)
    title_histo.draw(Win)

#column names
def subTitle(sub_title,Win,place,height_rec,n):
    x1,x2,y1,y2 = rectangle(n,place,height_rec,Win)
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

#histogram making
def histogram(pro_count,pro_m_count,dnp_count,excl_count):
    global sub_titles,place,tot_outcomes
    Win = GraphWin('histogram', 805, 600)
    Win.setBackground(color_rgb(237,242,236))
    linex = Line(Point(150,500),Point(655,500))
    tot_outcomes = pro_count + pro_m_count + dnp_count + excl_count
    n = col_height(pro_count,pro_m_count,dnp_count,excl_count)
    title(Win)
    #display columns
    for height_rec in (pro_count,pro_m_count,dnp_count,excl_count):
        col_colours(place)
        rectangle(n,place,height_rec/n,Win)
        sub_title = sub_titles[place-1]
        subTitle(sub_title,Win,place,height_rec,n)
        place += 1
    linex.draw(Win)
    Win.getMouse()
    Win.close()