import turtle
t = turtle.Turtle()
t.speed(1)

for i in range(3):
    t.forward(100)
    t.left(120)
    
t.goto(30,0)

for i in range(3):  
    t.left(60)
    t.backward(500)
    
t.goto(60,0)

turtle.done()