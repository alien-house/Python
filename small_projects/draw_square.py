import turtle
def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")

    fig = turtle.Turtle()
    fig.shape("circle")
    fig.color("white")
    fig.speed(5)
    
    fig.forward(200)
    fig.right(90)
    fig.forward(200)
    fig.right(90)
    fig.forward(200)
    fig.right(90)
    fig.forward(200)
    fig.right(90)

    fig.right(10)
    
    fig.forward(200)
    fig.right(90)
    fig.forward(200)
    fig.right(90)
    fig.forward(200)
    fig.right(90)
    fig.forward(200)
    fig.right(90)

    #fig2 = turtle.Turtle()
    #fig2.shape("arrow")
    #fig2.circle(100)
    
    window.exitonclick()

draw_square()
