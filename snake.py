import turtle as trt
import time
import random

#setting up windows screen
win=trt.Screen()
win.title("Snake Game By Kumail Abbas")
win.bgcolor("black")
win.setup(width=600,height=600)
win.tracer(0)

#creating head
head=trt.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.penup()
head.goto(0,0)
head.direction="stop"

#creating food
food=trt.Turtle()
food.speed(0)
food.color("red")
food.shape("circle")
food.shapesize(0.7)
food.penup()
food.goto(0,100)

#creating score
count=0

score=trt.Turtle()
score.speed(0)
score.shape("square")
score.hideturtle()
score.goto(0,290)
score.color("white")
score.write("Score: {}".format(count))
score.penup()



#moving functions
def up():
    head.direction="up"
def down():
    head.direction="down"
def left():
    head.direction="left"
def right():
    head.direction="right"



def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)
    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)
    if head.direction=="right":
        x=head.xcor()
        head.setx(x+20)
    if head.direction=="left":
        x=head.xcor()
        head.setx(x-20) 
win.listen()
win.onkeypress(up,"w")
win.onkeypress(down,"s")
win.onkeypress(left,"a")
win.onkeypress(right,"d")

body=[]
while True:
    win.update()
    move()
    time.sleep(0.1)
    #going out from the screen logic
    if head.xcor()>300:
        x=head.xcor()-600
        head.setx(x)
    if head.xcor()<-300:
        x=head.xcor()+600
        head.setx(x)
    if head.ycor()>300:
        y=head.ycor()-600
        head.sety(y)
    if head.ycor()<-300:
        y=head.ycor()+600
        head.sety(y)
#head coliding with food
    if head.distance(food) < 20:
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)
        count=count+1
        score.clear()
        score.write("Score: {}".format(count))
        score.penup()
        #creating new body
        newbody=trt.Turtle()
        newbody.shape("square")
        newbody.color("white")
        newbody.speed(0)
        newbody.penup()
        body.append(newbody)
        #body moving according to its previous one
    for i in range(len(body)-1,0,-1):
        x=body[i-1].xcor()
        y=body[i-1].ycor()
        body[i].goto(x,y)
    if len(body)>0:
        x=head.xcor()
        y=head.ycor()
        body[0].goto(x,y)
    for i in body:
        if i.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"
            count=0
            score.clear
            score.write("SCORE: {}".format(count))
            for i in body:
                i.goto(1000,1000)
            body.clear()


print(count)
win.mainloop()