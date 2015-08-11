#!/usr/bin/env python
# HW05_ex00_TextAdventure.py
##############################################################################
# Imports
import sys
from sys import exit

# Body


def infinite_stairway_room(count=0):
    name=sys.argv[1]
    print "%s walks through the door to see a dimly lit hallway." %name
    print "At the end of the hallway is a", count * 'long ', 'staircase going towards some light'
    next = raw_input("> ")
    
    # infinite stairs option
    if next == "take stairs":
        print '%s takes the stairs' %name
        if (count > 0):
            print "but %s is not happy about it" %name
        infinite_stairway_room(count + 1)
    # option 2 == ?????
    if next == 'Stop' or next=='stop':
        dead("This infinite neverending staircase epitomizes your infinite greed. You will forever seek penance for your sins on this staircase !")
    


def gold_room():
    name=sys.argv[1]
    print "This room is full of gold.  How much does %s take?" %name

    next = raw_input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, learn to type a number.")

    if how_much < 100:
        print "Nice, %s is not greedy, he takes the gold and goes back home!" %name
        exit(0)
    else:
        print "Oh! A greedy guy! A new shiny door opened up which can make you the richest person alive. Go for it? "  #If the user is greedy, we give him an even greedier option, to take the attractive door which would lead him to the infinite staircase.
        next1= raw_input("> ")
        if next1== "yes" or next1=="Yes":
            infinite_stairway_room(count=0)
        else:
            dead("You decided to take the money. A pit opened up below you and you died ! ")        #If this time round, the user does not take the even greedier option, we give him an easier ending - which is to kill him instantly, instead of letting him rot in the staircase forever.


def bear_room():
    name=sys.argv[1]
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How is %s going to move the bear?" %name
    bear_moved = False

    while True:
        next = raw_input("> ")

        if next == "take" or next == "honey":
            dead("The bear looks at you then slaps your face off.")
        elif next == "taunt" and not bear_moved:
            print "The bear has moved from the door. %s can go through it now." %name
            bear_moved = True
        elif next == "taunt" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif (next == "open" or next =="door") and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means."


def cthulhu_room():
    name=sys.argv[1]
    print "Here %s sees the great evil Cthulhu." %name
    print "He, it, whatever stares at %s and he goes insane." %name
    print "Does %s flee for his life or eat his head?" %name

    next = raw_input("> ")

    if "flee" in next:
        main()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print why, "Good job!"
    exit(0)


##############################################################################
def main():
    # START the TextAdventure game
    name=sys.argv[1]
    print "%s is in a dark room." %name
    print "There is a door to his right and left."
    print "Which one does %s take?" %name

    next = raw_input("> ")

    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

if __name__ == '__main__':
    main()
