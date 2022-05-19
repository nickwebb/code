#!/usr/bin/env python3

import random

def getIdea(ideaNumber):
    if ideaNumber == 1:
        return 'make the riff work over chord changes'
    elif ideaNumber == 2:
        return 'repeat one note through chord changes'
    elif ideaNumber == 3:
        return 'extra 5th in bass'
    elif ideaNumber == 4:
        return 'hold for an extra bar'
    elif ideaNumber == 5:
        return 'mute to get interesting rhythm'
    elif ideaNumber == 6:
        return 'up an octave!'
    elif ideaNumber == 7:
        return 'slide'
    elif ideaNumber == 8:
        return 'gallop'
    elif ideaNumber == 9:
        return 'have the base chord you want and add b6, 5, b4'
    elif ideaNumber == 10:
        return 'tremolo it'
    elif ideaNumber == 11:
        return 'arp it babe'
    
r = random.randint(1,11)
    
print("Ok, it's riffin time. Let's try...")

riffIdea = getIdea(r)    
print(riffIdea)
    
print('and')

r = random.randint(1,11)    
riffIdea = getIdea(r)
print(riffIdea)
    
print('and')

r = random.randint(1,11)    
riffIdea = getIdea(r)
print(riffIdea)