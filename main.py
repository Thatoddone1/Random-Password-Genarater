import random
import string
times = input('Enter The Nuber Of Password(s) You Want To Genarate: ')
length = input('Enter The Length Of the Password(s): ')
wantLower = input('Do you want lower case letters in the password(s)')
wantUpper = input('Do you want upper case lestters in the password(s)')
wantNum = input('Do you want numbers in the password(s)')



b = 0
i = 0
c = random.randint(1,3)
while b < int(times):
    while i < int(length):
        if c == 1:
            print(random.choice(string.ascii_lowercase), end='')
        elif c == 2:
            print(random.randint(1,9), end='')
        elif c == 3:
            print(random.choice(string.ascii_uppercase), end='')
        i = i+1
        c = random.randint(1,3)
            
    print('')
    i = 0
    b = b+1
    
