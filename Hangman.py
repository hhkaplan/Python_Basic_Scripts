#Hangman! Hangwoman! Equal opportunity hanging!
import random
from tkinter import *

#Here's the list of words and the computer chooses one of them
wordlist = ["mouse", "camera", "hatchet", "willow", "spike", "television",
            "simple", "ugly", "comical","thermos","rose","cabinet","hello",
            "treasure","vampire","academia","research","veritable","yellow",
            "wanderlust", "aphrodisiac", "oyster","turntable","try"]
theword = random.choice(wordlist)
print(theword, "just for now...")

#Create a board
def createboard(word):
    x = len(word)
    print("_ "*x)

#Check a letter against the word
def checkletter(word, letter):
    out = 1
    letlist = list(word)
    newlist =["-"]*len(word)
    newlist = [x if x == letter else 0 for x in letlist]
    if newlist != [0]*len(word): #update out# to reflect match(0) v no match (1)
        out = 0
    return newlist, out

#Update the board with a guess
def updateboard(oldlist, newlist):
    onemorelist =["_"]*len(oldlist)
    for num,name in enumerate(newlist):
        if isinstance(name, str):
            oldlist[num] = name
    onemorelist = oldlist
    return onemorelist

#Create the hanged person adding a shape each turn
def updatehangwoman(interface, count):
    if count == 1:
        interface.create_oval(80, 30, 100, 50) #head
        w.update()
    if count == 2:
        interface.create_line(90, 50, 90, 80) #body
        w.update()
    if count == 3:
        interface.create_line(90, 80, 80, 100) #leg1
        w.update()
    if count == 4:
        interface.create_line(90, 80, 100, 100) #leg2
        w.update()
    if count == 5:
        interface.create_line(90, 65, 80, 60) #arm1
        w.update()
    if count == 6:
        interface.create_line(90, 65, 100, 60) #arm2
        w.update()
    if count == 7:
        interface.create_line(87, 42, 93,42) #mouth
        w.update()
    if count == 8:
        interface.create_oval(85, 36, 88, 38) #eye1
        w.update()
    if count == 9:
         interface.create_oval(92, 36, 95, 38) #eye2
         w.update()
        
#Now to make it all run...

#Draw the board original board
master = Tk()
w = Canvas(master, width=200, height=200)
w.create_line(10, 150, 90, 150)
w.create_line(50, 150, 50, 20)
w.create_line(50, 20, 90, 20)
w.create_line(90, 20, 90, 30)
w.pack()
w.update()

#Print spaces for the word
print("Here's your board:")
createboard(theword)

#Initialize a bunch of variables to be changed in the while loop
match = list(theword)
count = 0
newlist = [0]*len(theword)
oldlist = ["_"]*len(theword)

while match != oldlist and count < 9:
    theletter = input("Guess a letter: ")   
    letterlist, out = checkletter(theword, theletter) #Find matching letters
    fulllist = updateboard(oldlist, letterlist) #Update board with letters
    print(' '.join(fulllist)) #Reprint the board
    oldlist = fulllist #Rename board
    
    count = count + out #Count incorrect tries
    if count == 8:
        print("Last chance...")
        
    updatehangwoman(w, count) #update the image
    
#Tell them how they did 
if count == 9:
    print("YOU LOSE")
else:       
    print("WINNER!")

