__author__ = 'halley'
from music21 import stream, chord, note

scale = [0,2,4,5,7,9,11] #standard C-major scale
octave = 5

#some common progressions
progressions_base_1 = [[1,4,5,1],[1,4,5,6],[1,5,6,4], [1,2,5,1]]
progressions_base_0 = [[root - 1 for root in progression] for progression in progressions_base_1]

score = stream.Score()

for progression in progressions_base_0:
    for chord_root in progression:

        #get triad starting at root
        root = scale[chord_root] + octave*12
        if chord_root + 2 < len(scale):
            third = scale[chord_root + 2] + (octave*12)
        else:
            third = scale[(chord_root + 2) % 7] + (octave + 1) * 12
        if chord_root + 4 < len(scale):
            fifth = scale[chord_root + 4] + (octave*12)
        else:
            fifth = scale[(chord_root + 4) % 7] + (octave + 1) * 12
        notes_in_chord = [note.Note(pitch) for pitch in [root, third, fifth]]

        #combine into 2-beat chord
        c = chord.Chord(notes_in_chord)
        c.quarterLength = 2.0

        score.append(c)

score.show(fmt='midi')
