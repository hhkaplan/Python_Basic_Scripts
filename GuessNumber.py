#Here's a fun game: the computer generates a number and you guess that number
import random

#Get user to enter range from which to guess
var1, var2 = input("Enter the range you'd like to guess from (# #): ").split()

#Make sure range is valid, make it valid if it isn't
if var1 > var2:
    print("Expected lowest value first; numbers re-ordered in range.")
    var1n = int(var2)
    var2n = int(var1)
elif var1 == var2:
    print("Invalid range, default set to 0 - 10")
    var1n = 0
    var2n = 10
else:
    var1n = int(var1)
    var2n = int(var2)

#Generate a number
number = random.randint(var1n, var2n)

count = 1
n = 0
while n == 0:

    #Ask for a guess
    yourguess = input("What number is the computer thinking of between {} and {}? ".format(var1n, var2n))
    try:
       yourguess = int(yourguess)
    except: 
        print("Sorry! The number was {}".format(number))
        break
    
    #Compare guess to # and respond accordingly
    if int(yourguess) == number:
        n = 1
        print("You guessed right! The number is {} and you got there in {} turn(s)!".format(yourguess, count))
    elif yourguess < number:
        print ("Your guess is too low, guess again")
    elif yourguess > number:
        print("Your guess is too high, guess again")
    else:
        n = 1
        
    count +=1
    if count == 3:
        print("*Hint: To give up, enter a letter*")


    





        
