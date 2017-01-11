#Learning Python: Rolling dice

#Define the number of sides on your dice
sides = input('How many sides does your dice have (e.g. 6, 8, 10, 12, 20)? ')
sides = int(sides)
print('Rolling your' ,sides,'-sided dice...')

#Set up a loop to keep the dice rolls comin'
rolly = 'y'
while rolly =='y':

    #Use randint to generate a number between 1 and #sides
    import random
    randnum = random.randint(0, sides)
    print(randnum)
    
    #Ask to roll again
    rolly = input('Roll again? y or n: ')

print('Thanks for playing!')

