__author__ = 'halley'
import random
from music21 import stream, note

note_count = 60 #total notes

scale = [0,2,4,5,7,9,11] #standard C scale
octave = 5

#initialize pitch and duration
degrees = [random.randint(0,14) for i in range(0, note_count)]
pitches = [scale[degree % 7] + (octave+(degree/7))*12 for degree in degrees]
durs = [random.choice([0.5,1.0,1.5,0.25,0.75]) for i in range(0, note_count)]



score = stream.Score()

for i in range(0, note_count):
    n = note.Note(pitches[i])
    n.quarterLength = durs[i]
    score.append(n)

score.show('midi')
