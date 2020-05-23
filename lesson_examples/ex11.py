from random import random
print('Enter your name:', end=' ')
x = input()
print(f'Hello, ' + x,'\b, that\'s a nice name.', end=' ')
result = False
while (result != True):
    print('Now, pick a number 1-10:')
    y = input()
    print(f'Excellent, ' + y,'\b is a great number. Let\'s roll the dice.')
    r = random()
    ro = ((round(r, 1)) * 10)
    rr = (int(ro))
    roll = ('You rolled: {}')
    print(roll.format(rr))
    result = (roll == rr)
    print(result)
if result == True:
    print('You win!')
    break
print('Game over.')
