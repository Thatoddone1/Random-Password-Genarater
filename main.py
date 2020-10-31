import random
import string

i = 0
while i < 10:
    print(random.choice(string.ascii_letters), end='')
    i = i+1
print('')
