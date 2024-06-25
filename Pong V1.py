import turtle


class Paddle(turtle.Turtle):
    def __init__(self, speed = 0, shape = str, color = str):
        super().__init__()
        self.speed(0)
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()


paddle1 = Paddle()
paddle1.goto(-350,0)


paddle2 = Paddle()
paddle2.goto(350,0)


## Window ##
window = turtle.Screen()
window.title("Pong V.1")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0) ## Stops window from updating ##


## Score ##
score1 = 0
score2 = 0


##Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("yellow")
ball.penup()
ball.goto(0,0)
ball.dx = .10 # everytime ball moves, it moves by 2 pixels in x ##
ball.dy = -.10


# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.goto(0,260)
pen.hideturtle()
pen.clear()
pen.write(f"Player 1: {score1}" +  f"     Player 2: {score2}", align = "center", font =("arial", 24, "bold"))




# FUNCTION
def paddle_1_up():
    y = paddle1.ycor() # finds current y coordinate of paddle1
    y += 30 # adds 20 px to y coordinate ##
    paddle1.sety(y) # sets new Y location to the new Y location (+=20)


def paddle_1_down():
    y = paddle1.ycor() # finds current y coordinate of paddle1 ##
    y -= 30 # subtracts 20 px to y coordinate ##
    paddle1.sety(y) # sets new Y location to the new Y location (+=20)


def paddle_2_up():
    y = paddle2.ycor()
    y += 30
    paddle2.sety(y)


def paddle_2_down():
    y = paddle2.ycor()
    y -= 30
    paddle2.sety(y)


# Function
window.listen() ## Tells CPU to listen for keyboard
window.onkeypress(paddle_1_up, "w")
window.onkeypress(paddle_1_down, "s")
window.onkeypress(paddle_2_up, "o")
window.onkeypress(paddle_2_down, "l")


# Main game loop
while True:
    window.update() # everytime the loop runs, the screen updates##


    # MOVE THE BALL
    ball.setx(ball.xcor() + ball.dx) # combining current x coordinate plus ball direction on x ##
    ball.sety(ball.ycor() + ball.dy)


    # Border
    if ball.ycor() > 290: # if current ball y coordinate is greater than 290##
        ball.sety(290)
        ball.dy *= -1 # reverses the direction of the ball
    if paddle1.ycor() > 290: # Prevents paddle from floating out of bounds
        paddle1.sety(290)
    if paddle2.ycor() > 290:
        paddle2.sety(290)        


    if ball.ycor() < -290: # if current ball y coordinate is greater than 290##
        ball.sety(-290)
        ball.dy *= -1 # reverses the direction of the ball
    if paddle1.ycor() < -290: # Prevents paddle from floating out of bounds
        paddle1.sety(-290)
    if paddle2.ycor() < -290:
        paddle2.sety(-290)  
   
   # adds score to scoreboard when ball reaches beyond goal area
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score1 += 1
        pen.clear()
        pen.write(f"Player 1: {score1}" +  f"     Player 2: {score2}", align = "center", font =("arial", 24, "bold"))
   
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score2 += 1
        pen.clear()
        pen.write(f"Player 1: {score1}" +  f"     Player 2: {score2}", align = "center", font =("arial", 24, "bold"))


    # paddle + ball collision
    if (ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() < paddle2.ycor() + 40 and ball.ycor() > paddle2.ycor() -50):
        ball.setx(340)
        ball.dx *= -1


    if (ball.xcor() < -340 and ball.xcor() < -350 and ball.ycor() < paddle1.ycor() + 40 and ball.ycor() > paddle1.ycor() -50):
        ball.setx(-340)
        ball.dx *= -1
