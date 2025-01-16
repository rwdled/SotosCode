import turtle as tmuncher
import random
import keyboard

player = input('''Please select an option
                1. Play
                2. Login
                3. View Leaderboard ''' )


   
def newgame():
   #list for turtle expansion
   trtleextend = [tmuncher.Turtle(shape="square"), tmuncher.Turtle(shape="square")]
   
   newttrt = tmuncher.Turtle(shape="turtle")
   newttrt.penup()
   newttrt.color("black")

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
        for i in range(0, len(trtleextend) - 1,1):
            trtleextend[i].goto(trtleextend[i - 1].position())
        trtleextend[0].goto(newttrt.position())

   def point():
         if check_collision(newttrt, apple):
            apple.setposition(random.randint(-250, 250), random.randint(-250, 250))
            trtleextend.append(tmuncher.Turtle(shape="turtle"))
            add_turtle()

        #controls    
   def move_and_check():
      newttrt.forward(25)
      point()
      move_turtles()
      tmuncher.ontime(move_and_check, 250)
   
   tmuncher.listen()
   move_and_check()
   tmuncher.onkey(lambda: newttrt.left(90), "a")
   tmuncher.onkey(lambda: newttrt.right(90), "d")
   move_and_check()
   tmuncher.done()

if player == "1":
   newgame()
  
   

   
