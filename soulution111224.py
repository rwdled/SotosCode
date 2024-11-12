import turtle
import random
# Create a list of colors
colors = ["red", "green", "blue", "yellow", "purple", "orange"]

# Function to create and return a turtle with random color and position
def create_turtle():
    t = turtle.Turtle(shape="turtle")
    t.color(random.choice(colors))
    t.penup()
    t.goto(random.randint(-250, 250), random.randint(-250, 250))
    t.setheading(random.randint(0, 360))  # Random initial direction
    return t

# Create a list of turtles
turtles = [create_turtle() for _ in range(4)]

# Function to check if two turtles are close enough to collide
def check_collision(t1, t2):
    return t1.distance(t2) < 20

# Function to move turtles and handle collisions
def move_turtles():
    while True:
        for t in turtles:
            t.forward(10)
            
            # Bounce off walls
            if t.xcor() > 290 or t.xcor() < -290:
                t.setheading(180 - t.heading())
            if t.ycor() > 290 or t.ycor() < -290:
                t.setheading(360 - t.heading())
            
            # Check for collisions with other turtles
            for other_turtle in turtles:
                if t != other_turtle and check_collision(t, other_turtle):
                    t.color(random.choice(colors))
                    other_turtle.color(random.choice(colors))
        
       

# Turn off automatic screen updates for smooth animation


# Start moving turtles
move_turtles()

# Keep the window open
turtle.done()

