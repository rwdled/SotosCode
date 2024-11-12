import turtle as trt1
import random
t1  = trt1.Turtle()
t2 = trt1.Turtle()
t3 = trt1.Turtle()
t4 = trt1.Turtle()
t1.penup()
t1.setposition(300,200)
t1.color("red")

t2.penup()
t2.setposition(0,100)
t2.color("blue")

t3.penup()
t3.setposition(150,200)
t3.color("green")

t4.penup()
t4.setposition(60,20)
t4.color("orange")
for i in range(10):
    for i in range(20):
        t1.pendown()
        t1.forward(random.randint(-45,100))
        t1.right(random.randint(0,180))

    #for i in range(20):
        t2.pendown()
        t2.forward(random.randint(-45,100))
        t2.right(random.randint(0,180))

    #for i in range(20):
        t3.pendown()
        t3.forward(random.randint(-45,100))
        t3.right(random.randint(0,180))


    #for i in range(20):
        t4.pendown()
        t4.forward(random.randint(-45,100))
        t4.right(random.randint(0,180))




