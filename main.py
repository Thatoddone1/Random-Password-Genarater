import random
import string
times = input('Enter The Nuber Of Password(s) You Want To Genarate: ')
length = input('Enter The Length Of the Password(s): ')

b = 0
i = 0
while b < int(times):
    while i < int(length):
        if random.randint(1,2) == 1:
            print(random.choice(string.ascii_letters), end='')
            i = i+1
        else:
            print(random.randint(1,9), end='')
            i = i+1
    print('')
    i = 0
    b = b+1
    
