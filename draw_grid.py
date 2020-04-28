import turtle

def init_grid(n):
    global w
    w = 400 / n
    turtle.speed('fastest')
    turtle.screensize()
    turtle.penup()
    turtle.pencolor('black')
    turtle.pensize(1)
    for i in range(n+1):
        turtle.goto(-200, -200+w*i)
        turtle.pendown()
        turtle.forward(n*w)  
        turtle.penup()
    
    turtle.left(90)
    for i in range(n+1):
        turtle.goto(-200+w*i, -200)
        turtle.pendown()
        turtle.forward(n*w)
        turtle.penup()
    turtle.hideturtle()

# pedestrian: red cell
def color_p(n, x, y):
    a = -200 + (x-1)*w
    b = -200 + (n-y)*w
    turtle.goto(a, b)
    turtle.fillcolor('red')
    turtle.begin_fill()
    for _ in range(4):            
        turtle.left(90)
        turtle.backward(w-0.5)
    turtle.end_fill()
    turtle.hideturtle()

# target: yellow cell
def color_t(n, x, y):
    a = -200 + (x-1)*w
    b = -200 + (n-y)*w
    turtle.goto(a, b)
    turtle.fillcolor('yellow')
    turtle.begin_fill()
    for _ in range(4):            
        turtle.left(90)
        turtle.backward(w-0.5)
    turtle.end_fill()
    turtle.hideturtle()

# obstacle: violet cell
def color_o(n, x, y):
    a = -200 + (x-1)*w
    b = -200 + (n-y)*w
    turtle.goto(a, b)
    turtle.fillcolor('violet')
    turtle.begin_fill()
    for _ in range(4):            
        turtle.left(90)
        turtle.backward(w-0.5)
    turtle.end_fill()
    turtle.hideturtle()

# empty: white cell
def color_e(n, x, y):
    a = -200 + (x-1)*w
    b = -200 + (n-y)*w
    turtle.goto(a, b)
    turtle.fillcolor('white')
    turtle.begin_fill()
    for _ in range(4):            
        turtle.left(90)
        turtle.backward(w-0.5)
    turtle.end_fill()
    turtle.hideturtle()