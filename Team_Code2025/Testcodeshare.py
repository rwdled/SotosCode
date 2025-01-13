import turtle as tmuncher
import random
import keyboard

player = input('''Please select an option
                1. Play
                2. Login
                3. View Leaderboard ''' )


   
def newgame():
   #total_score   
   def check_collision(check1, check2):
      return check1.distance(check2) < 20
   total_score = 0


   #Game element (Circle)
   #tmuncher.bgcolor("black")
   
   apple = tmuncher.Turtle(shape="circle")
   apple.color("red")
   #apple.penup()
   apple.setposition(random.randint(-250, 250), random.randint(-250, 250))

   #check for collision 
      
   newttrt = tmuncher.Turtle(shape="turtle")
   newttrt.penup()
   # move then check for collision
   def point():
         if check_collision(newttrt, apple):
            apple.setposition(random.randint(-250, 250), random.randint(-250, 250))
            total_score += 1
            print(total_score)
   
   #Controls
   tmuncher.listen()
   tmuncher.onkey(lambda: newttrt.left(90), "a")
   tmuncher.onkey(lambda: newttrt.forward(25), "w")
   tmuncher.onkey(lambda: newttrt.backward(25), "s")
   tmuncher.onkey(lambda: newttrt.right(90), "d")
   



if player == "1":
   newgame()
   

   
tmuncher.done()