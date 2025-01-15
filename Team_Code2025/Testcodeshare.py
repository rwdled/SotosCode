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
   while True:
      trtleextend[1].setposition(-1, newttrt.ycor())
     trtleextend[0].setposition(-1, newttrt.ycor())
     break
   newttrt.penup()
   
   apple = tmuncher.Turtle(shape="circle")
   apple.color("red")
   apple.penup()
   apple.setposition(random.randint(-250, 250), random.randint(-250, 250))
  
   def check_collision(check1, check2):
      return check1.distance(check2) < 20
   def point():
         if check_collision(newttrt, apple):
            apple.setposition(random.randint(-250, 250), random.randint(-250, 250))
            trtleextend.append(tmuncher.Turtle(shape="turtle"))
            
            
               
        #controls    
   def move_and_check():
      newttrt.forward(25)
      point()
   tmuncher.listen()
   tmuncher.onkey(lambda: newttrt.left(90), "a")
   tmuncher.onkey(move_and_check, "w")
   #tmuncher.onkey(lambda: newttrt.backward(25), "s")
   tmuncher.onkey(lambda: newttrt.right(90), "d")
   point()
   tmuncher.done()
if player == "1":
   newgame()
  
   

   
