import turtle
import time

wn = turtle.Screen()
wn.title("Dinosaur")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score = 0
# Make Dino

# Dino Tail Tip
dino_tail_tip = turtle.Turtle()
dino_tail_tip.speed(0)
dino_tail_tip.shape("square")
dino_tail_tip.color("red")
dino_tail_tip.shapesize(stretch_wid=.4, stretch_len = 2.5)
dino_tail_tip.penup()
dino_tail_tip.tilt(-20)
dino_tail_tip.goto(-200, -3)

# Dino Tail
dino_tail = turtle.Turtle()
dino_tail.speed(0)
dino_tail.shape("square")
dino_tail.color("orange")
dino_tail.shapesize(stretch_wid=.8, stretch_len = 3)
dino_tail.penup()
dino_tail.tilt(-10)
dino_tail.goto(-150, -15)

# Dino Body
dino_body = turtle.Turtle()
dino_body.speed(0)
dino_body.shape("square")
dino_body.color("red")
dino_body.shapesize(stretch_wid=2, stretch_len = 6)
dino_body.penup()
dino_body.goto(-75, -25)

# Dino Neck
dino_neck = turtle.Turtle()
dino_neck.speed(0)
dino_neck.shape("triangle")
dino_neck.color("orange")
dino_neck.penup()
dino_neck.goto(-10, -20)

# Dino Head
dino_head = turtle.Turtle()
dino_head.speed(0)
dino_head.shape("square")
dino_head.color("red")
dino_head.shapesize(stretch_wid=2, stretch_len = 4)
dino_head.penup()
dino_head.goto(0, 0)

# Dino Eye
dino_eye = turtle.Turtle()
dino_eye.speed(0)
dino_eye.shape("square")
dino_eye.color("blue")
dino_eye.shapesize(stretch_wid=.5, stretch_len = .5)
dino_eye.penup()
dino_eye.goto(-10, 5)

# Draw Dino
def draw_dino(locatex, locatey):
    locatex = int(locatex)
    locatey = int(locatey)
    dino_body.goto(locatex + -75, locatey + -25)
    dino_neck.goto(locatex + -10, locatey + -20)
    dino_head.goto(locatex, locatey)
    dino_eye.goto(locatex + -10, locatey + 5)
    dino_tail.goto(locatex + -150, locatey + -15)
    dino_tail_tip.goto(locatex + -200, locatey + -3)
    
# Test the Dino (remove later)
draw_dino(200, 50)

# Functions


# Keyboard Binding


# Main Game Loop
while True:
    wn.update()