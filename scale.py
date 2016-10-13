__author__ = 'halley'
from music21 import stream, note

pitch_classes = [0,2,4,5,7,9,11,12] #standard C scale
octave = 5
pitches = [octave*12 + pitch_class for pitch_class in pitch_classes]

score = stream.Score()

for pitch in pitches:
    n = note.Note(pitch)
    n.quarterLength = 1.0
    score.append(n)

score.show(fmt='midi')