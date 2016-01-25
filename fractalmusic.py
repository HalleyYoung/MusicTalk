# -*- coding: utf-8 -*-
"""
Created on Tue Nov 18 14:55:55 2014

@author: halley
"""
from noteconstants import *
from music21 import *
import pitchhelpers as pth
"""
rules can be chords - schenkerian analysis in terms of l system

make each rule 2-beats
make each rule have a certain chance of changing

"""


rules = {}
rules["A"] = ["A-6", "B-2", "Gs-6", "A-2"]
rules["B"] = ["B-8", "A-2", "C-2", "B-4"]
rules["C"] = ["C-8", "Gs-4", "A-4"]
rules["D"] = ["D-6", "E-2", "A-4", "Gs-2"]
rules["E"] = ["A-8", "F-6", "E-2"]
rules["F"] = ["F-8", "E-4", "F-4"]
rules["Gs"] = ["Gs-4", "A-8", "B-4"]

def genLSystem(iterations, start_array, rules):
    #print('start_array ' + str(start_array))
    if (iterations == 1):
        return start_array
    else:
        new_array = []
        for i in range(0, len(start_array)):
            item = start_array[i]
            #print('item ' + str(item))
            if item[0] in rules:
                new_array.extend(genLSystem(iterations - 1, rules[item.split('-')[0]], rules))
            else:
                new_array.append(item)
        return new_array

def notesFromRuleOutput(routput):
    notes = []
    for i in range(0, len(routput)):
        new_note = note.Note()
        if i > 1:
            new_note.midi = pth.getClosestPC(notes[-1].midi, midi_notes[routput[i].split('-')[0]])
        else:
            new_note.midi = midi_notes[routput[i].split('-')[0]] + 72
        new_note.quarterLength = int(routput[i][-1])/4.0
        notes.append(new_note)
    return notes

def fixNoteLens(notes):
    new_notes = []
    cur_rhythm = 0
    for note in notes:
        r = note.quarterLength
        if r + cur_rhythm == 4.0:
            cur_rhythm = 0
            new_notes.append(note)
        elif r + cur_rhythm > 4.0:
            note.quarterLength = 4.0 - cur_rhythm
            cur_rhythm = 0
            new_notes.append(note)
        else:
            new_notes.append(note)
            cur_rhythm += r
    return new_notes

start_array = ["A-8", "E-8", "Gs-8", "A-8"]
iterations = 4
g = genLSystem(iterations, start_array, rules)
notes = notesFromRuleOutput(g)
score = stream.Stream()
score.append(notes)
score.show('musicxml')