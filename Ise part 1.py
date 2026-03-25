from music21 import * #This imports the music21 library which is essential for this project
environment.set('musicxmlPath', r'C:\Program Files\MuseScore 4\bin\MuseScore4.exe') #The set destination for the file to be sent to and the type of file that it will be saved as
n = note.Note('C4') #This is middle C, a note of great importance in music
n.quarterLength = 2 #This initialises the note length as a minim, a note that lasts 2 beats
n.show() #This is for displaying the information in musescore

