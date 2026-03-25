from music21 import * #This imports the music21 library which is essential for this project
environment.set('musicxmlPath', r'C:\Program Files\MuseScore 4\bin\MuseScore4.exe') #The set destination for the file to be sent to and the type of file that it will be saved as
s = stream.Stream()#This now acts as a list this is the score that we will add all the notes and instruments to
s.append(meter.TimeSignature('3/4')) #This adds a time signature to the piece, this is important so the software knows how to divide up the bars of music
s.append(note.Note('C4'))
s.append(note.Note('D4'))
s.append(note.Note('E4'))#These 3 notes will be added to the list s to then be added to the musicxml file
s.show()