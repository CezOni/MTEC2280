import sys, random

#Starting features
state = 0

intExplore = input("Welcome, you have fallen through the ground of the ruins while visiting on vacation. You are currently trapped in a stoned dark room. Some light escapes from the deep hole you fell through but only enough for a dim room. Type explore to search the room. ")
#test input
#print(intExplore)

var1 = str('Explore')

if (state == 0):

	if (intExplore == var1):
		intSearch = input("There are some rocks, a gem on a pedestal, bones lying around, and a door. Which one you like to search? ")
		state = 1

	else:
		print("Sorry, you have no other options at the moment. Would you like to explore now? ")
		state  = 0

rocks = str('rocks')
gem = str('a gem on a pedestal')
bones = str('bones')
door = str('door')

if (intSearch == rocks):
	intSearch = input("Not much around here. What would you like to search now? ")
#Multiple "Sorry invalid option appeared."
#else:
	#print("Sorry invalid option.")
	#state = 1

if (intSearch == gem):
	intSearch = input("Not much around here. What would you like to search now? ")

#else:
	#print("Sorry invalid option.")
	#state = 1

if (intSearch == door):
	intSearch = input("The door looks locked. What would you like to search now? ")

#else:
	#print("Sorry invalid option.")
	#state = 1

if (intSearch == bones):
	intSearch = input("You found a key! What would you like to search now? ")
	unlocked = door

#else:
	#print("Sorry invalid option.")
	#state = 1

#Tomb2
if (intSearch == unlocked):
	print("You unlocked the door. On the other side is a valley and a exit on the other side. You can search either left or right. Where would you like to go?")
	state = 2

if(state == 2):
        intDirection = input("Where would you like to search? ")


        if(intDirection == "right"):
            print("You found a moldy potato under some rocks!")
            state = 3
            intDirection = input("Would you like to check the other side or go back in the middle? ")
            if intDirection = middle
            	state = 5

            elif intDirection = other side
            	state = 6

        elif(command == "left"):
            print("You found some wooden planks. You can use this to build a bridge!")
            state = 4
            intDirection = input("Would you like to check the other side or go back in the middle? ")
            if intDirection = middle
            	state = 5

            elif intDirection = other side
            	state = 7
    
        if(state = 6):
            print("You found some wooden planks. You can use this to build a bridge!")
            state = 3
            intDirection = input("Would you like to check the other side or go back in the middle? ")
            if intDirection = middle
            	state = 5

            elif intDirection = other side
            	state = 6

         if(state = 7):
            print("You found a moldy potato under some rocks!")
            state = 3
            intDirection = input("Would you like to check the other side or go back in the middle? ")
            if intDirection = middle
            	state = 8

            elif intDirection = other side
            	state = 6

        else:
            print("Wrong input")
            state = 2

#Tomb3
if (state == 8):

	print("There's a mummy blocking a hallway! What would you like to do?")

intMummy = input ("Run, Fight, or Feed?")

run = str(Run)
fight = str(Fight)
feed = str(feed)

if (intMummy == run):

print("You ran but the mummy has caught you")

elif (intMummy == fight):

print("The mummy has killed you.")

elif (intMummy == feed):

print("The mummy is eating the moldy potato. You have run around it while it's distracted.")
state = 9

else

print("Invalid input")

if (state == 9):

input("Type and enter any key to exit game: ")