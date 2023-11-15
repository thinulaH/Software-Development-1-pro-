from graphics import *
win = GraphWin("chart", 800, 600)
linex = Line(Point(200,450),Point(600,450))
liney = Line(Point(200,450),Point(200,100))
j = ['Malli','Akki','Ammi','Thaththi']
x = 0
for i in ["thinula","inuri","Pushpa","Ranjith"]:
    print(x)
    print(j[x], i)
    x = x + 1

linex.draw(win)
liney.draw(win)

win.getMouse() # pause for click in window
win.close()
