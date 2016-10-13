__author__ = 'halley'
from music21 import note

pitch_class = 0
octave = 5
pitch = octave*12 + pitch_class
duration = 4.0

n = note.Note(pitch)
n.quarterLength = duration

n.show()