from graphics import *



def main():
    win = GraphWin("Graph",700,700)
    
    aPoint = Point(320,320)
    aPoint.draw(win)

    aLine = Line(Point(360,350),Point(320,320))
    aLine.draw(win)

    aLine2 = Line(Point(50,50),Point(590,50))
    aLine2.draw(win)

    aCircle = Circle(Point(320,320),60)
    aCircle.setFill(color_rgb(163,54,36))
    aCircle.draw(win)


    rec1 = Rectangle(Point(650,50),Point(550,590))
    rec1.setFill("black")
    rec1.draw(win)

    rec2 = Rectangle(Point(50,50),Point(150,590))
    rec2.setFill("black")
    rec2.draw(win)

        
    win.getMouse()
    win.close()                

main()
    
