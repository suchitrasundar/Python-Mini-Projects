import turtle
def draw_square(some_turtle):
    for i in range (1,5):
        some_turtle.forward(100)
        some_turtle.right(90)


def draw_art():
    window=turtle.Screen()
    window.bgcolor("blue")
    
    x=turtle.Turtle()
    x.shape("classic")
    x.color("white")
    x.speed(10)
    for i in range (1,37) :
        draw_square(x)
        x.right(10)

    #y = turtle.Turtle()
    #y.shape("classic")
    #y.color("white")
    #y.speed(3)
    #y.circle(100)

    window.exitonclick()

draw_art()
draw_square()
