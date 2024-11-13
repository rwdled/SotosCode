import turtle as trt1
import random
colors = ["red", "green", "blue", "yellow", "purple", "orange"]
def newtrt():
    newguy = trt1.Turtle(shape="turtle")
    newguy.color(random.choice(colors))
    newguy.penup()
    newguy.setposition(random.randint(-250, 250), random.randint(-250, 250))
    newguy.setheading(random.randint(0, 360)) 
    newguy.pendown()
    return newguy
turtles = [newtrt() for uhhh in range(4)]
def check_collision(check1, check2):
    return check1.distance(check2) < 20
def move():
    while True:
        for newguy in turtles:
            newguy.forward(10)
            if newguy.xcor() > 300 or newguy.xcor() < -320:
                newguy.setheading(180 - newguy.heading())
            if newguy.ycor() > 290 or newguy.ycor() < -290:
                newguy.setheading(360 - newguy.heading())
            for other in turtles:
                if newguy != other and check_collision(newguy, other):
                    newguy.color(random.choice(colors))
                    other.color(random.choice(colors))
trt1.Screen().bgcolor("black")
move()



