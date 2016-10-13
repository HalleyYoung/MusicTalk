__author__ = 'halley'
from music21 import stream, note, chord

#scale notes
root_pitch_classes = [0,2,4,5,7,9,11,12]
octave = 5

chord_pitches = []

#add first, third, and fifth of the chord
for i in range(0, len(root_pitch_classes)):
    root = root_pitch_classes[i] + octave*12
    if i + 2 < len(root_pitch_classes):
        third = root_pitch_classes[i + 2] + (octave*12)
    else:
        third = root_pitch_classes[(i + 2) % 7] + (octave + 1) * 12
    if i + 4 < len(root_pitch_classes):
        fifth = root_pitch_classes[i + 4] + (octave*12)
    else:
        fifth = root_pitch_classes[(i + 4) % 7] + (octave + 1) * 12
    chord_pitches.append((root, third, fifth))

score = stream.Score()

#add chords to score
chords = []
for i in range(0, len(chord_pitches)):
    print(chord_pitches[i])
    notes = [note.Note(pitch) for pitch in chord_pitches[i]]
    print([i.pitch.midi for i in notes])
    c = chord.Chord(notes)
    c.quarterLength = 2.0
    chords.append(c)

score.append(chords)
score.show('midi')