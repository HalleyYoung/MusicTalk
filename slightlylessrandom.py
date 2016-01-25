__author__ = 'halley'
import random
from music21 import *

two_beat_rhythms = [[1.0,1.0], [0.5,0.5,0.5,0.5], [1.5,0.5], [2.0]] #options for rhythm

durations = []
degrees = []
previous_note = 0
for i in range(0,20):
    two_beat_rhythm = random.choice(two_beat_rhythms) #randomly pick one rhythm
    for j in range(0, len(two_beat_rhythm)): #for each note in the rhythm, choose a pitch by moving from the previous pitch
        degrees.append(previous_note + random.choice([-2,-1,0,1,2]))
        previous_note = degrees[-1]
    durations.extend(two_beat_rhythm)

scale = [0,2,4,5,7,9,11]

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