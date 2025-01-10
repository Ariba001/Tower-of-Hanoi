import turtle
import colorsys

# Setup the screen and turtle
turtle.setup(800, 600)
turtle.hideturtle()
turtle.title("Tower of Hanoi")
turtle.speed(0)
turtle.tracer(0, 0)

# Configuration
n = 9  # Number of rings
peg_height = 300
ring_height = 20
ring_width = 100  # Same width for all rings
animation_step = 10

# Pegs (initially empty)
A = []
B = []
C = []

# Turtle objects for rings
T = []

# Colors for the rings
colors = ["Darkviolet", "pink", "blue"]

# Function to draw a line (for the pegs and base)
def draw_line(x, y, heading, length, pensize, color):
    turtle.up()
    turtle.goto(x, y)
    turtle.seth(heading)
    turtle.down()
    turtle.color(color)
    turtle.pensize(pensize)
    turtle.fd(length)

# Draw the initial scene (base and pegs)
def draw_scene():
    turtle.bgcolor('light blue')
    draw_line(-600, -100, 0, 1200, 10, 'brown')
    for i in range(-250, 251, 250):
        draw_line(i, -93, 90, peg_height, 5, 'black')

# Initialize the rings and their positions
def initialize():
    for i in range(n):
        t = turtle.Turtle()
        t.hideturtle()
        t.speed(0)
        t.pencolor('black')
        t.fillcolor(colors[i % len(colors)])  # Assign colors
        T.append(t)
    
    # Distribute rings among the rods
    A.extend([0, 1, 2])  # Red rings on A
    B.extend([3, 4, 5])  # Green rings on B
    C.extend([6, 7, 8])  # Blue rings on C

# Draw a single ring
def draw_single_ring(r, x, k, extra=0):
    T[r].up()
    T[r].goto(x - ring_width / 2, -95 + ring_height * k + extra)
    T[r].down()
    T[r].seth(0)
    T[r].begin_fill()
    for i in range(2):
        T[r].fd(ring_width)
        T[r].left(90)
        T[r].fd(ring_height)
        T[r].left(90)
    T[r].end_fill()

# Draw all rings
def draw_rings():
    for i in range(len(A)):
        draw_single_ring(A[i], -250, i)
    for i in range(len(B)):
        draw_single_ring(B[i], 0, i)
    for i in range(len(C)):
        draw_single_ring(C[i], 250, i)

# Move a ring from one peg to another with animation
def move_ring(PP, QQ):
    if PP == "A":
        x = -250
        P = A
    elif PP == "B":
        x = 0
        P = B
    else:
        x = 250
        P = C

    if QQ == "A":
        x2 = -250
        Q = A
    elif QQ == "B":
        x2 = 0
        Q = B
    else:
        x2 = 250
        Q = C

    # Animation for lifting the ring
    for extra in range(1, 250 - (-95 + ring_height * (len(P) - 1)), animation_step):
        T[P[-1]].clear()
        draw_single_ring(P[-1], x, len(P) - 1, extra)
        turtle.update()

    T[P[-1]].clear()
    draw_single_ring(P[-1], x, len(P) - 1, extra)
    turtle.update()

    tp = x
    step = animation_step if x2 > x else -animation_step
    for tp in range(x, x2, step):
        T[P[-1]].clear()
        draw_single_ring(P[-1], tp, len(P) - 1, extra)
        turtle.update()

    T[P[-1]].clear()
    draw_single_ring(P[-1], x2, len(P) - 1, extra)
    turtle.update()
    
    Q.append(P.pop())
    
    # Animation for lowering the ring
    for extra in range(250 - (-95 + ring_height * (len(Q) - 1)), 0, -animation_step):
        T[Q[-1]].clear()
        draw_single_ring(Q[-1], x2, len(Q) - 1, extra)
        turtle.update()

    T[Q[-1]].clear()
    draw_single_ring(Q[-1], x2, len(Q) - 1)
    turtle.update()

# Recursive function to solve the Tower of Hanoi
def tower_of_hanoi(X, Y, Z, n):
    if n == 1:
        move_ring(X, Z)
        return
    tower_of_hanoi(X, Z, Y, n - 1)
    move_ring(X, Z)
    tower_of_hanoi(Y, X, Z, n - 1)

# Key bindings for manual ring movement
def move_rings_with_keys():
    def move_left():
        move_ring("A", "B")
        draw_rings()

    def move_right():
        move_ring("B", "C")
        draw_rings()

    def move_up():
        move_ring("C", "A")
        draw_rings()

    turtle.listen()
    turtle.onkey(move_left, "Left")
    turtle.onkey(move_right, "Right")
    turtle.onkey(move_up, "Up")

    def game_over():
        turtle.penup()
        turtle.goto(0, 0)
        turtle.write("Game Over", align="center", font=("Arial", 24, "normal"))
        turtle.update()
        turtle.bye()

    turtle.onkey(game_over, "Tab")

draw_scene()
turtle.update()
initialize()
draw_rings()
move_rings_with_keys()
turtle.update()
turtle.mainloop()
