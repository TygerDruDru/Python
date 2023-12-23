import turtle

wn = turtle.Screen()
wn.title("Slime Jumper")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score = 0

# Slime Head
slime_head = turtle.Turtle()
slime_head.speed(0)
slime_head.shape("square")
slime_head.color("light green")
slime_head.penup()
slime_head.goto(0, 0)

# Slime Eye
slime_eye = turtle.Turtle()
slime_eye.speed(0)
slime_eye.shape("square")
slime_eye.color("blue")
slime_eye.shapesize(stretch_wid=.25, stretch_len = .25)
slime_eye.penup()
slime_eye.goto(0, 0)

# Main Game Loop
while True:
    wn.update()
    