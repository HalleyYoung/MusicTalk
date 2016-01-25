__author__ = 'halley'
from music21 import *
import scale as sc

root_notes = [0,1,3,4,5,0,4,0] #lowest notes in the chord
durations = [2.0,1.0,1.0,2.0,1.0,1.0,2.0,2.0]

chord_degrees = [(root_note, root_note + 2, root_note + 4) for root_note in root_notes]

scale = [0,2,4,7,9,11] #pitches in the scale

chords = []
for i in range(0, len(chord_pitches)):
    chord_notes = []
    for degree in chord_degrees[i]:
        n = note.Note(scale[degree % 7] + ((degree/7) + 5) * 12)
        n.quarterLength = durations[i]
        chord_notes.append(n)
    c = chord.Chord(chord_notes)
    chords.append(c)

s = stream.Score()
s.append(chords)
s.show()