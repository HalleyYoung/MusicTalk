__author__ = 'halley'
#generating a single note
from music21 import *

n = note.Note("C4") # a 'C' note, 4th octave
n.quarterLength = 1.0 # a quarter note, worth 1 beat

part = stream.Part()
part.insert(0, n) #insert note into part

score = stream.Score()
score.insert(0, part) #insert part into score

score.show()