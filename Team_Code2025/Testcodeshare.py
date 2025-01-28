import turtle as tmuncher
import random
import keyboard
import time
import os

player = input('''Please select an option
                1. Play
                2. Login
''' )


def newgame():
   points = 0
   #list for turtle expansion
   trtleextend = [tmuncher.Turtle(shape="square"), tmuncher.Turtle(shape="square")]
   
   newttrt = tmuncher.Turtle(shape="turtle")
   newttrt.penup()
   newttrt.color("black")

   #apple
   apple = tmuncher.Turtle(shape="circle")
   apple.color("red")
   apple.penup()
   apple.setposition(random.randint(-250, 249), random.randint(-250, 250))
  
   def check_collision(check1, check2):
      return check1.distance(check2) < 20
   
   def add_turtle():
        new_turtle = tmuncher.Turtle(shape="square")
        new_turtle.penup()
        trtleextend.append(new_turtle)

   def move_turtles():
        for i in range(len(trtleextend) - 1, 0, -1):
            trtleextend[i].goto(trtleextend[i - 1].position())
        trtleextend[0].goto(newttrt.position())

   def point(z):
         if check_collision(newttrt, apple):
            apple.setposition(random.randint(-250, 250), random.randint(-250, 250))
            add_turtle()
            #return z + 1
   while True:
      tmuncher.listen()
      tmuncher.onkey(lambda: newttrt.left(90), "a")
      tmuncher.onkey(lambda: newttrt.right(90), "d")
      tmuncher.onkey(lambda: newttrt.forward(25), "w")
      tmuncher.onkey(lambda: newttrt.backward(25), "s")
      move_turtles()
      points = point(points)
      tmuncher.update()
      newttrt.forward(20)
      time.sleep(0.1)
      if newttrt.xcor() > 500 or newttrt.xcor() < -500 or newttrt.ycor() > 500 or newttrt.ycor() < -500:
         print("ran into the wall, Game is ober. you had " + str(points) + " points")
         break
      for i in range(1, len(trtleextend)):
         if check_collision(newttrt, trtleextend[i]):
            print("ran into yourself, Game is ober. you had " + str(points) + " points")
            break
   #      controls    your a faggot :) - jordin&ben
   
   

   
   tmuncher.done()

if player == "1":
   newgame()
  
   

   
