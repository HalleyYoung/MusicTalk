__author__ = 'halley'
#generating a scale
from music21 import *


degrees = range(0,8) #an ascending scale of degrees

scale = [0,2,4,5,7,9,11] #pitches in the scale

notes = []


for i in range(0, len(degrees)):
    #convert scale degree to pitch
    pitch = scale[degrees[i] % 7] + ((degrees[i]/7) + 5) * 12
    new_note = note.Note(pitch)
    new_note.quarterLength = 4.0 #all whole notes worth 4 beats
    notes.append(new_note)

score = stream.Score()
score.append(notes)
score.show()