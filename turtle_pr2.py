import turtle

# s=turtle.getscreen()
t=turtle.Turtle()

colors=[
    'red',
    'purple',
    'purple',
    'blue',
    'green',
    'orange',
    'yellow'
]
# t.turtle.Pen()
turtle.bgcolor('black')
for x in range(360):
    t.pencolor(colors[x%6])
    t.width(x/100+1)
    t.fd(x)
    t.left(59)
