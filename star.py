import turtle


my_turtle = turtle.Turtle()
counter = 0
def star():
    my_turtle.forward(100)
    my_turtle.right(90)
    my_turtle.forward(100)
    my_turtle.right(90)
    my_turtle.forward(100)
    my_turtle.right(90)
    my_turtle.forward(100)
    my_turtle.right(100)


for i in range(36):
    counter = i
    print(counter)
    star()
    


