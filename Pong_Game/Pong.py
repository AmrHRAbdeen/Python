###################################################################
# @Desc.: Pong Game
# @Author: Amr Abdeen
# @IDE: Visual Studio Code
# @Python Version: 3.8.2
# @Packages: tkinter [sudo apt-get install python3-tk]
###################################################################

#### import Packages ###
import turtle as tr

### Private Variables ###
AScore=0
BScore=0

#Create Window
wn=tr.Screen()
wn.title("Pong Game")
wn.bgcolor("black")
wn.setup(width=800,height=600)
#Stops the window form moving -> Speed the game up
wn.tracer(0)

# Game Objects
# Paddle A
paddle_a=tr.Turtle()
#Animation Speed (0 = Max)
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=4,stretch_len=1)
paddle_a.penup()
# Window Center is 0,0
paddle_a.goto(+350,0)
# Paddle B
paddle_b=tr.Turtle()
#Animation Speed (0 = Max)
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=4,stretch_len=1)
paddle_b.penup()
# Window Center is 0,0
paddle_b.goto(-350,0)
# Ball
ball=tr.Turtle()
#Animation Speed (0 = Max)
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)

# Define Functions
def paddle_state(paddleName,paddleState):
    #To Move Paddle A we need the coordinates
    # Get Y Axis
    if((paddleName =='paddle_a') and (paddleState=='up')):
        # Move paddle a up by 20 pixels
        y= paddle_a.ycor()
        y +=20
        paddle_a.sety(y)
    elif ((paddleName =='paddle_a') and (paddleState=='down')):
        y= paddle_a.ycor()
        y -=20
        paddle_a.sety(y)
    elif ((paddleName =='paddle_b') and (paddleState=='up')):
        # Move paddle a up by 20 pixels
        y= paddle_b.ycor()
        y +=20
        paddle_b.sety(y)
    elif ((paddleName =='paddle_b') and (paddleState=='down')):
        y= paddle_b.ycor()
        y -=20
        paddle_b.sety(y)    
# Move paddle_a
def movePaddleAFun_down():
    paddle_state('paddle_a','down')
def movePaddleAFun_up():
    paddle_state('paddle_a','up')
def movePaddleBFun_down():
    paddle_state('paddle_b','down')
def movePaddleBFun_up():
    paddle_state('paddle_b','up')        
# Keyboard Inputs
wn.listen()
wn.onkeypress(movePaddleAFun_up,"w")
wn.onkeypress(movePaddleAFun_down,"s")
wn.onkeypress(movePaddleBFun_up,"Up")
wn.onkeypress(movePaddleBFun_down,"Down")

#Moving the Ball
# Moving in X axis
ball.dx=0.25
# Moving in Y axis
ball.dy=0.25

# Adding Scoring
score = tr.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0,260)
score.write("Player A: %d     Player B: %d "%(AScore,BScore),align="center",font=("Arial",15))
#Main Game Super Loop
while True:
    wn.update()
    # Move the ball 
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    #Boarder Checking 
    #Top and Bottom Boarders
    if (ball.ycor() > 290):
        ball.sety(290)
        ball.dy*=-1
    if (ball.ycor() < -290):
        ball.sety(-290)
        ball.dy*=-1    
    #Left and Right Boarders
    if (ball.xcor() > 390):
        ball.setx(390)
        ball.dx*=-1
        BScore+=1
        score.clear()
        score.write("Player A: {}     Player B: {} ".format(AScore,BScore),align="center",font=("Arial",15))
    if (ball.xcor() < -390):
        ball.setx(-390)
        ball.dx*=-1  
        AScore+=1
        score.clear()
        score.write("Player A: %d     Player B: %d "%(AScore,BScore),align="center",font=("Arial",15))     
    # Paddle and Ball collisions
    # Cosidrations: Window [ 800 * 600 ] & (0,0) is the center
    # Ball width = 10 px , paddle = (10px * 50px)
    # Object origin from its center
    # Paddles @ +/- 350 px in x-axis
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 20 and ball.ycor() > paddle_b.ycor() -20):
        ball.dx *=-1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 20 and ball.ycor() > paddle_a.ycor() -20):
        BScore+=1
    
