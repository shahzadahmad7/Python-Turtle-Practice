import turtle
t=turtle.Turtle()

t.speed(10)
for i in range(180):
    t.fd(100)
    t.rt(30)

    t.fd(20)
    t.rt(60)

    t.fd(50)
    t.rt(20)

t.penup()
t.setpos(0,0)
t.pendown()
t.right(2)

turtle.done()