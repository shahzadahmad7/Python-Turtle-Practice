import turtle
#initialize screen
s=turtle.getscreen()
#setting color & title
s.bgcolor("yellow")
s.title("My turtle")

#To move turtle we use farward(fd), backward(bk), right(rt) and left(lt)
t=turtle.Turtle()
t.rt(30)
t.fd(90)
t.lt(30)
t.bk(90)
#If we consider screen as XY-plane and our tutle at origin(0,0), we can move turtle with goto(x,y)
t.goto(30,30)
#return home/origin
t.home()