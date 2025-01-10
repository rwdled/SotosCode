import turtle as tmuncher
import random
import keyboard

player = input('''Please select an option
                1. Play
                2. Login
                3. View Leaderboard ''' )


   
def newgame():
   newttrt = tmuncher.Turtle(shape="turtle")
   #newttrt.color()
   newttrt.penup()
   #Controls
   
   tmuncher.listen()
   tmuncher.onkey(lambda: newttrt.left(180), "a")
   tmuncher.onkey(lambda: newttrt.forward(100), "w")
   tmuncher.onkey(lambda: newttrt.backward(100), "s")
   tmuncher.onkey(lambda: newttrt.right(90), "d")
         


if player == "1":
   newgame()
   

   
tmuncher.done()