__author__ = 'halley'
from music21 import stream, chord, note
import random

scale = [0,2,4,5,7,9,11] #Our standard C-major scale
bass_octave = 4
treble_octave = 5

progressions_base_1 = [[1,4,5,1],[1,4,5,6],[1,5,6,4], [1,2,5,1]]
progressions_base_0 = [[chord - 1 for chord in progression] for progression in progressions_base_1]

score = stream.Score()
part1 = stream.Part()
part2 = stream.Part()

half_measure_rhythms = ([[1.5,0.5], [1.5,0.25,0.25], [1.0,1.0], [1.0,0.5,0.5], [0.5,0.5,1.0]])


prev_pitch = 60 #used to make sure we don't leap too far
#loop through progressions
for progression in progressions_base_0:
    for chord_root in progression:
        #get pitch classes of chord notes
        pcs = [scale[i % 7] for i in [chord_root, chord_root + 2, chord_root + 4]]
        pitches_w_octaves = filter(lambda i: i%12 in pcs, range(60,84))

        #choose durations
        treble_rhythm = random.choice(half_measure_rhythms)
        for dur in treble_rhythm:
            #get notes in chord close to the previous degree
            notes_in_chord_close_to_prev_degree = filter(lambda i: abs(i - prev_pitch < 7), pitches_w_octaves)
            current_pitch = random.choice(notes_in_chord_close_to_prev_degree)
            n = note.Note(current_pitch)
            n.quarterLength = dur
            part1.append(n)

        #now create bass chord
        root = scale[chord_root] + bass_octave*12
        if chord_root + 2 < len(scale):
            third = scale[chord_root + 2] + (bass_octave*12)
        else:
            third = scale[(chord_root + 2) % 7] + (bass_octave + 1) * 12
        if chord_root + 4 < len(scale):
            fifth = scale[chord_root + 4] + (bass_octave*12)
        else:
            fifth = scale[(chord_root + 4) % 7] + (bass_octave + 1) * 12
        notes_in_chord = [note.Note(pitch) for pitch in [root, third, fifth]]

        c = chord.Chord(notes_in_chord)
        c.quarterLength = 2.0

        part2.append(c)

#insert parts
score.insert(0, part1)
score.insert(0, part2)

score.show(fmt='midi')
