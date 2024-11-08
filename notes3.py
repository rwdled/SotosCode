#string_Methods

#Strings: Sequence of characters, basically List

sQuote_string = 'Hello' # we can create a sting by using ''
print(sQuote_string)
doubleQuote =  "ello" #common way
MutiString = ''' THis is a multi
line
string'''
print("______________________________________________________")

#common String Method
# len() : Returns length of the string (num of char)
greet = "Ello mate"
print(len(greet)) # 9 Char

#lower() : converts the string to all lowercase
print(greet.lower()) #output "ello mate" - this is very helpful when you compare  strings to each other

#upper() : coverts string to all uppercase

print(greet.upper())

print("______________________________________________________")

#Strip() : Removes any front and end spaces
Greeting = "   ALL   "
print(Greeting.strip())
print(Greeting)

print("______________________________________________________")

#replace(): replacing a phrasing with another new phrase
print(greet.replace("mate", "fella"))
print(greet)
print("______________________________________________________")

#--
a = "hello"
a.replace("l" , " ")
print(a)
# STRINGS ARE IMMUATABLE | STRINGS CANNOT BE CHANGED UNLESS THEY GET A RESEOANBLE CHARACTER

#split(): the string from a sepcified delimiter and outputs as a list

print(greet.split())
print(greet.split("l")) #Removes the "l" from list

#join()Revserse of split(), but its diff
print(greet.join("E" "mate"))

wombat = ["Womg" "domg" "Kong"]
print("b".join(wombat))

#find(): searches the string for value
#postion of where it found(first time) (index) , -1 if not found
wan = "ello, World"
print(wan.find("ello,"))
print(wan.find("World"))

#Count. Startwith()., Endwith() -slicing adn index