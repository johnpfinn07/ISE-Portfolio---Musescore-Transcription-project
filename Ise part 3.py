from music21 import * #This imports the music21 library which is essential for this project
environment.set('musicxmlPath', r'C:\Program Files\MuseScore 4\bin\MuseScore4.exe') #The set destination for the file to be sent to and the type of file that it will be saved as

s = stream.Stream()#This now acts as a list, this is the score that we will add all the notes and instruments to

part1 = stream.Part()

part2 = stream.Part()

part3 = stream.Part()

part4 = stream.Part()
#These are the 4 parts that I will be adding to the score, these act as different lines on the sheet of music
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
part1.append(voice1)
part2.append(voice2)
part3.append(voice3)
part4.append(voice4)
#The 4 voices are added to the four parts, this is essential for further iterations as it allows me to create full melody lines and then add them to the parts in future.
s.insert(0, part1)
s.insert(0, part2)
s.insert(0, part3)
s.insert(0, part4)
#The parts are now added to the score
s.show()
#The score is now displayed in musescore