__author__ = 'halley'
#generating a piece of music consisting of random notes

import random
from music21 import *

degrees = []
durations = []

scale = [0,2,4,5,7,9,11]

for i in range(0,40): #repeatedly pick new pitch and duration
    degrees.append(random.randint(0,14))
    durations.append(random.choice([0.5,1.0,2.0]))

notes = []

for i in range(0, len(degrees)):
    #convert scale degree to pitch
    pitch = scale[degrees[i] % 7] + ((degrees[i]/7) + 5) * 12
    new_note = note.Note(pitch)
    new_note.quarterLength = durations[i] #add duration to note
    notes.append(new_note)

score = stream.Score()
score.append(notes)
score.show()