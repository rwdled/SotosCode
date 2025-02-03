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