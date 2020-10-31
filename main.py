#importing lib's
#they are all built in lib's
import random
import string
#asking the user qustions
times = input('Enter The Nuber Of Password(s) You Want To Genarate: ')
length = input('Enter The Length Of the Password(s): ')
wantLower = input('Do you want lower case letters in the password(s) (y/n)')
wantUpper = input('Do you want upper case lestters in the password(s) (y/n)')
wantNum = input('Do you want numbers in the password(s) (y/n)')
wantPunc = input('Do you want punctuation in the password(s (y/n))')


#checking to make sure that at least one option is on
if wantLower == 'n' and wantUpper == 'n' and wantNum == 'n' and wantPunc == 'n':
    print('Cant have all digets and charecters set to no')
    quit()

#setting all b and i to 0
b = 0
i = 0
#setting the first rand int
c = random.randint(1,4)
while b < int(times):
    while i < int(length):
        if c == 1 and wantLower == 'y':
            print(random.choice(string.ascii_lowercase), end='')
            i = i+1
        elif c == 2 and wantNum == 'y':
            print(random.randint(1,9), end='')
            i = i+1
        elif c == 3 and wantUpper == 'y':
            print(random.choice(string.ascii_uppercase), end='')
            i = i+1
        elif c == 4 and wantPunc == 'y':
            print(random.choice(string.punctuation), end='')
            i = i+1
        elif wantPunc == 'n' or wantNum == 'n' or wantUpper == 'n' or wantLower == 'n':
            pass
        else:
            print('error invalid value')
        c = random.randint(1,4)
            
    print('')
    i = 0
    b = b+1
    
