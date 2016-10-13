__author__ = 'halley'
import random
from music21 import stream, note

scale = [0,2,4,5,7,9,11] #standard C-major scale
octave = 6

total_measures = 16

#possible rhythms that span half a measure
half_measure_rhythms = ([[1.5,0.5], [1.5,0.25,0.25], [1.0,1.0], [1.0,0.5,0.5], [0.5,0.5,1.0]])

durs = []
degrees = []
prev_degree = 0

for i in range(0, int(total_measures*2)):
    half_measure_rhythm = random.choice(half_measure_rhythms) #choose random rhythm for 2 beats
    for dur in half_measure_rhythm:
        durs.append(dur)
        degrees.append(prev_degree + random.choice([-1,1,-1,1,0,-2,2])) #move a small, randomly chosen amount
        prev_degree = degrees[-1]

pitches = [scale[degree % 7] + (octave+(degree/7))*12 for degree in degrees] #convert degrees to pitches

#append to score
score = stream.Score()

for i in range(0, len(pitches)):
    n = note.Note(pitches[i])
    n.quarterLength = durs[i]
    score.append(n)

score.show('midi')
