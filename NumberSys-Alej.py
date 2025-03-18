
#hexadecimal chart:
# 0 1 2 3 4 5 6 7 8 9 A B C D E F
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
#base 16

#binary chart:
# 256 128 64 32 16 8 4 2 1
#base 2







def dec2bin(n):
    if n == 0:
        return '0'
    elif n == 1:
        return '1'
    else:
        return dec2bin(n//2) + str(n%2)

print(dec2bin(6))