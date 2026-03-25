from music21 import * #This imports the music21 library which is essential for this project
environment.set('musicxmlPath', r'C:\Program Files\MuseScore 4\bin\MuseScore4.exe') #The set destination for the file to be sent to and the type of file that it will be saved as

s = stream.Stream()#This now acts as a list, this is the score that we will add all the notes and instruments to

violin1 = stream.Part()

violin2 = stream.Part()

violin3 = stream.Part()

cello = stream.Part()
#I have now changed my variable names to their instrumental counterparts but still must change how they are viewed on the finished product

violin1.partName = "Violin I"

violin2.partName = "Violin II"

violin3.partName = "Violin III"

cello.partName = "Cello"

voice1 = stream.Voice()
voice2 = stream.Voice()
voice3 = stream.Voice()
voice4 = stream.Voice()
#This is to in itialise the different voices, they are the melody lines that will be added to the different parts
notes = ["C4","D4","E4","F4","G4","A4","B4","C5"]
#This is a list for the notes of the C major scale, they will be used as an example for the notes in my melody
for notename in notes:
    melody_note = note.Note(notename)
    voice1.append(melody_note)
    
    
    harmony_note = melody_note.transpose(-8)
    voice2.append(harmony_note)
    
    
    harmony_note1 = melody_note.transpose(-6)
    voice3.append(harmony_note1)
    
    harmony_note2 = melody_note.transpose(-4)
    voice4.append(harmony_note2)
#This while loop sets the first note as a fixed value being the scale of C major and transposes the scale with the intervals shown, the new notes are then added to each voice
violin1.append(voice1)
violin2.append(voice2)
violin3.append(voice3)
cello.append(voice4)
#The 4 voices are added to the four parts, this is essential for further iterations as it allows me to create full melody lines and then add them to the parts in future.
s.insert(0, violin1)
s.insert(0, violin2)
s.insert(0, violin3)
s.insert(0, cello)
#The parts are now added to the score
s.show()
#The score is now displayed in musescore