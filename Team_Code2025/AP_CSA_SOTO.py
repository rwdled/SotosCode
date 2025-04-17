import turtle as tmuncher
import random
import keyboard
import time

player = input('''Please select an option
                1. Play

''' )
speedopt = int(input('''Please select an option
                1. Slow
                2. Medium
                3. Fast

''' ))

   
#TODO Add speed function 

 # procedure with parameter, for loops with if statements. 
def newgame(speed):
   #setup screen
   points = 0
   square = tmuncher.Turtle(shape="square")
   square2 = tmuncher.Turtle(shape="square")
   trtleextend = [square, square2]
   square.penup()
   
   newttrt = tmuncher.Turtle(shape="turtle")
   newttrt.penup()
   newttrt.color("black")
   addpoint = 0

   #apple
   apple = tmuncher.Turtle(shape="circle")
   apple.color("red")
   apple.penup()
   apple.setposition(random.randint(-250, 250), random.randint(-250, 250))

  
  
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

   def point():
         while newttrt.distance(apple) < 20:
            if check_collision(newttrt, apple):
               apple.setposition(random.randint(-250, 250), random.randint(-250, 250))
               add_turtle()
               return addpoint + 1
   while True:
      tmuncher.listen()
      tmuncher.onkey(lambda: newttrt.left(90), "a")
      tmuncher.onkey(lambda: newttrt.right(90), "d")
      tmuncher.onkey(lambda: newttrt.forward(25), "w")
      tmuncher.onkey(lambda: newttrt.backward(25), "s")
      move_turtles()
      points = point()
      tmuncher.update()
      newttrt.forward(speed)
      time.sleep(0.1)
      if newttrt.xcor() > 500 or newttrt.xcor() < -500 or newttrt.ycor() > 500 or newttrt.ycor() < -500:
         print("ran into the wall, Game is ober. you had " + str(points) + " points")
         tmuncher.bye()
         break
      for i in range(1, len(trtleextend)):
         if check_collision(newttrt, trtleextend[i]):
            print("ran into yourself, Game is ober. you had " + str(points) + " points")
            tmuncher.bye()
            break
   tmuncher.done()

if player == "1":
   speed = 20
   if(speedopt == 1):
       speed = 10
   elif(speedopt == 2):
         speed = 20
   elif(speedopt == 3):
         speed = 30
   else:
         print("Invalid option, defaulting to speed 20")
         speed = 20
   newgame(speed)
  
  

   
