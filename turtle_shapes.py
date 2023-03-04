import turtle

s=turtle.getscreen()
t=turtle.Turtle()

#Drawing filled circle with dot(radius)
t.dot(100)

#we can draw a circle(radius)
t.circle(30)
#square
t.forward(100)
t.right(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)
#triangle
t.goto(-100,0)
t.goto(0,-100)
t.goto(100,0)
t.goto(0,0)