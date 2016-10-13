__author__ = 'halley'
from music21 import stream, note
import random

scale = [0,2,4,5,7,9,11] #Our standard C-major scale
octave = 6
half_measure_rhythms = ([[1.5,0.5], [1.5,0.25,0.25], [1.0,1.0], [1.0,0.5,0.5], [0.5,0.5,1.0]])

score = stream.Score()

all_durations = []
all_degrees = []

for i in range(0,4):
    #get the first measure of the phrase
    base_measure_rhythm = random.choice(half_measure_rhythms) + random.choice(half_measure_rhythms)
    prev_degree = 0
    base_measure_degrees = []
    for dur in base_measure_rhythm:
        base_measure_degrees.append(prev_degree + random.choice([-1,1,-1,1,2,-2,0]))
        prev_degree = base_measure_degrees[-1]
    #add first measure to the overall list
    all_durations.extend(base_measure_rhythm)
    all_degrees.extend(base_measure_degrees)

    #get the second measure - an inversion of the first
    second_measure_rhythm = base_measure_rhythm
    second_measure_degrees = [0]
    base_measure_intervals = [base_measure_degrees[i] - base_measure_degrees[i - 1] for i in range(1, len(base_measure_degrees))]
    inverted_intervals = [i*-1 for i in base_measure_intervals]
    for interval in inverted_intervals:
        second_measure_degrees.append(second_measure_degrees[-1] + interval)
    #add second measure to overall list
    all_durations.extend(second_measure_rhythm)
    all_degrees.extend(second_measure_degrees)

    #get the third measure - a transposition of the first
    third_measure_rhythm = base_measure_rhythm
    third_measure_degrees = [i + 1 for i in base_measure_degrees]
    #add third measure to overall list
    all_durations.extend(third_measure_rhythm)
    all_degrees.extend(third_measure_degrees)

    #get the fourth measure - a retrograde (reversal) of the first
    fourth_measure_rhythm = base_measure_rhythm[::-1]
    fourth_measure_degrees = base_measure_degrees[::-1]
    #add the fourth measure to the overall list
    all_durations.extend(fourth_measure_rhythm)
    all_degrees.extend(fourth_measure_degrees)

#create notes, add to score
for i in range(0, len(all_durations)):
    degree = all_degrees[i]
    pitch = scale[degree % 7] + (octave+degree/7)*12
    n = note.Note(pitch)
    n.quarterLength = all_durations[i]
    score.append(n)

score.show(fmt='midi')