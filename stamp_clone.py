import turtle
t=turtle.Turtle()
t.fd(100)
#stamp
t.stamp()

#clear stamp using stamp ID or location
t.clearstamp(4)

#clone
c=t.clone()
c.circle(40)
t.penup()
t.circle(100)
t.pendown()
t.circle(60)