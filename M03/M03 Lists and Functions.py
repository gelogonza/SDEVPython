#7.4
things = ["mozzarella", "cinderella", "salmonella"]

#7.5
things[1] = things[1].capitalize()
print(things)
#Yes the element "cinderella" changed to "Cinderella"

#7.6
things[0] = things[0].upper()
print (things)
#changed "mozzarella" to "MOZZARELLA"

#7.7
things.remove("salmonella")
print(things)
#result is ['MOZZARELLA', 'Cinderella']
#Collecting my Nobel Prize now!
 
#9.1
def good():
    return ['Harry', 'Ron', 'Hermione']

#9.2
def get_odds():
    for number in range(10):
        if number % 2 != 0:
            yield number
            
counter = 0
for number in get_odds():
    counter+= 1
    if counter == 3:
        print(number)
        break
 