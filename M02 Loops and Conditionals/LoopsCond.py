# 4.1
secret = 1
guess = 3

if guess < secret:
    print('too low')
elif guess > secret:
    print('too high')
else: 
    print('just right')


# 4.2
small = True
green = False

if small and green:
    print('its a pea')
elif not small and not green:
    print('its a pumpkin')
elif not small and green:
    print('its a watermelon')
else:
    print('its a cherry')


#6.1
numbers = [3, 2, 1, 0]

for number in numbers:
    print(number)
    
    
#6.2
guess_me = 7
number = 1

while True:
    if number < guess_me:
        print('too low')
    elif number == guess_me:
        print('found it!')
        break
    elif number > guess_me:
        print('oops')
        break
    number += 1
    
#6.3
guess_me = 5

for number in range(10):
    if number < guess_me:
        print('too low!')
    elif number == guess_me:
        print('found it!')
        break
    elif number > guess_me:
        print('oops')
        break