import turtle

def draw_square(t):
    for i in range(1,5):
        t.forward(100)
        t.right(90)

def draw_diamond(t):
    for i in range(1,3):
        t.forward(50)
        t.right(35)
        t.forward(50)
        t.right(145)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.fillcolor("black")
    brad.pencolor("yellow")
    brad.shape("turtle")
    brad.speed(0.5)
    
    i = 0
    while i < 360:    
        #draw_square(brad)
        draw_diamond(brad)
        brad.right(10)
        i = i + 10

    brad.right(90)
    brad.forward(200)

    window.exitonclick()

draw_art()
