
#hexadecimal chart:
# 0 1 2 3 4 5 6 7 8 9 A B C D E F
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
#base 16

#binary chart:
# 256 128 64 32 16 8 4 2 1
#base 2

userinput = input("Enter a number: ")
userinput = int(userinput)





def dec2bin(n):
    if n == 0:
        return '0'
    elif n == 1:
        return '1'
    else:
        return dec2bin(n//2) + str(n%2)
    
def dec2hex(n):
    if n == 0:
        return '0'
    elif n == 1:
        return '1'
    elif n == 2:
        return '2'
    elif n == 3:
        return '3'
    elif n == 4:
        return '4'
    elif n == 5:
        return '5'
    elif n == 6:
        return '6'
    elif n == 7:
        return '7'
    elif n == 8:
        return '8'
    elif n == 9:
        return '9'
    elif n == 10:
        return 'A'
    elif n == 11:
        return 'B'
    elif n == 12:
        return 'C'
    elif n == 13:
        return 'D'
    elif n == 14:
        return 'E'
    elif n == 15:
        return 'F'
    else:
        return dec2hex(n//16) + str(n%16)

print("Binary: ", dec2bin(userinput))
print("Hexadecimal: ", dec2hex(userinput))
print("Decimal: ", userinput)