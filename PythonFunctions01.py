# Function: A resuable block the performs a specific task
# function helps organize code, make it reusable, and reduce repetition

'''
def turn_right():
    turn_left()
    turn_left()
    turn_left()



    '''
name = "John"
name = "Jane"
# how to create a function
def greet():
    print("hello AP CSP")
    print("Today, we will learn about functions")


# how to call a function
greet() #calling a function
greet() #calling  it again
#greet()
print("-----------------")


#change it intp speific person greeting
# function/merhod overloading
def greet(person_name = ""):
    print("hello" + person_name)
    print("Today, we will learn about functions")

greet("Benjaimin")
greet()

def greet(person, subject):
    print("hello" + person)
    print("Today, we will learn about " + subject)

greet("Benjaimin", "Data Types")

# procedure mystery(number)
def rectangle_area(length, width):
    area = length * width
    print("The area of the rectangle is " + str(area))

rectangle_area(5, 10)
#one function that i can use in real life
#A function that i could use in real life is a function that calculates the area of a rectangle. 
# This function would take in the length and width of the rectangle as parameters and return the area of the rectangle as the outputThis function would be useful in a variety of situations, such as calculating the amount of paint needed to cover a wall or the amount of carpet needed to cover a floor. By creating a function to calculate the area of a rectangle, I can easily reuse this code whenever I need to calculate the area of a rectangle in the future.