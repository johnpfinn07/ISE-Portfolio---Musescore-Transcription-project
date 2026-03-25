from music21 import *

# Send output to MuseScore
environment.set('musicxmlPath', r'C:\Program Files\MuseScore 4\bin\MuseScore4.exe')

# Create score
s = stream.Score()

# Title and composer
s.metadata = metadata.Metadata()
s.metadata.title = "Jesu, Joy of Man's Desiring"
s.metadata.composer = "J.S Bach"

# Create parts
violin1 = stream.Part()
violin2 = stream.Part()
violin3 = stream.Part()
cello = stream.Part()

violin1.partName = "Violin 1"
violin2.partName = "Violin 2"
violin3.partName = "Violin 3"
cello.partName = "Violoncello"

# =========================
# BAR 1
# =========================

m1_v1 = stream.Measure(number=1)
m1_v2 = stream.Measure(number=1)
m1_v3 = stream.Measure(number=1)
m1_c = stream.Measure(number=1)

m1_v1.append(clef.TrebleClef())
m1_v1.append(key.KeySignature(1))
m1_v1.append(meter.TimeSignature("9/8"))
m1_v1.append(tempo.MetronomeMark(number=68, referent=duration.Duration(1.5)))

m1_v2.append(clef.TrebleClef())
m1_v2.append(key.KeySignature(1))
m1_v2.append(meter.TimeSignature("9/8"))

m1_v3.append(clef.TrebleClef())
m1_v3.append(key.KeySignature(1))
m1_v3.append(meter.TimeSignature("9/8"))

m1_c.append(clef.BassClef())
m1_c.append(key.KeySignature(1))
m1_c.append(meter.TimeSignature("9/8"))

# Violin 1
m1_v1.append(note.Rest(quarterLength=0.5))
m1_v1.append(note.Note("G4", quarterLength=0.5))
m1_v1.append(note.Note("A4", quarterLength=0.5))
m1_v1.append(note.Note("B4", quarterLength=0.5))
m1_v1.append(note.Note("D5", quarterLength=0.5))
m1_v1.append(note.Note("C5", quarterLength=0.5))
m1_v1.append(note.Note("C5", quarterLength=0.5))
m1_v1.append(note.Note("E5", quarterLength=0.5))
m1_v1.append(note.Note("D5", quarterLength=0.5))

# Violin 2
m1_v2.append(note.Rest(quarterLength=1))
m1_v2.append(note.Rest(quarterLength=0.5))
m1_v2.append(note.Note("G4", quarterLength=1.))
m1_v2.append(note.Note("F#4", quarterLength=0.5))
m1_v2.append(note.Note("G4", quarterLength=1.0))
m1_v2.append(note.Note("A4", quarterLength=0.5))

# Violin 3
m1_v3.append(note.Note("B3", quarterLength=1.5))
m1_v3.append(note.Note("D4", quarterLength=1.5))
m1_v3.append(note.Note("E4", quarterLength=1.5))

# Cello
m1_c.append(note.Note("G2", quarterLength=1.5))
m1_c.append(note.Note("G3", quarterLength=1.5))
m1_c.append(note.Note("E3", quarterLength=1.5))

# =========================
# BAR 2
# =========================

m2_v1 = stream.Measure(number=2)
m2_v2 = stream.Measure(number=2)
m2_v3 = stream.Measure(number=2)
m2_c = stream.Measure(number=2)

# Violin 1
m2_v1.append(note.Note("D5", quarterLength=0.5))
m2_v1.append(note.Note("G5", quarterLength=0.5))
m2_v1.append(note.Note("F#5", quarterLength=0.5))
m2_v1.append(note.Note("G5", quarterLength=0.5))
m2_v1.append(note.Note("D5", quarterLength=0.5))
m2_v1.append(note.Note("B4", quarterLength=0.5))
m2_v1.append(note.Note("G4", quarterLength=0.5))
m2_v1.append(note.Note("A4", quarterLength=0.5))
m2_v1.append(note.Note("B4", quarterLength=0.5))

# Violin 2
m2_v2.append(note.Note("B4", quarterLength=1))
m2_v2.append(note.Note("A4", quarterLength=0.5))
m2_v2.append(note.Note("B4", quarterLength=1))
m2_v2.append(note.Note("G4", quarterLength=0.5))
m2_v2.append(note.Note("E4", quarterLength=1))
m2_v2.append(note.Note("D4", quarterLength=0.5))

# Violin 3
m2_v3.append(note.Note("D4", quarterLength=1.5))
m2_v3.append(note.Note("E4", quarterLength=1.5))
m2_v3.append(note.Note("D4", quarterLength=1.5))

# Cello
m2_c.append(note.Note("B2", quarterLength=1.5))
m2_c.append(note.Note("E3", quarterLength=1.5))
m2_c.append(note.Note("C2", quarterLength=1.5))

# =========================
# BAR 3
# =========================

m3_v1 = stream.Measure(number=3)
m3_v2 = stream.Measure(number=3)
m3_v3 = stream.Measure(number=3)
m3_c = stream.Measure(number=3)

# Violin 1
m3_v1.append(note.Note("C5", quarterLength=0.5))
m3_v1.append(note.Note("D5", quarterLength=0.5))
m3_v1.append(note.Note("E5", quarterLength=0.5))
m3_v1.append(note.Note("D5", quarterLength=0.5))
m3_v1.append(note.Note("C5", quarterLength=0.5))
m3_v1.append(note.Note("B4", quarterLength=0.5))
m3_v1.append(note.Note("A4", quarterLength=0.5))
m3_v1.append(note.Note("B4", quarterLength=0.5))
m3_v1.append(note.Note("G4", quarterLength=0.5))

# Violin 2
m3_v2.append(note.Note("E4", quarterLength=1))
m3_v2.append(note.Note("F#4", quarterLength=0.5))
m3_v2.append(note.Note("G4", quarterLength=1))
m3_v2.append(note.Note("D4", quarterLength=0.5))
m3_v2.append(note.Note("E4", quarterLength=1))
m3_v2.append(note.Note("B3", quarterLength=0.5))

# Violin 3
m3_v3.append(note.Note("C4", quarterLength=1.5))
m3_v3.append(note.Note("B3", quarterLength=1.5))
m3_v3.append(note.Note("A3", quarterLength=1.5))

# Cello
m3_c.append(note.Note("A2", quarterLength=1.5))
m3_c.append(note.Note("B2", quarterLength=1.5))
m3_c.append(note.Note("C3", quarterLength=1.5))

# =========================
# ADD MEASURES TO PARTS
# =========================

violin1.append(m1_v1)
violin1.append(m2_v1)
violin1.append(m3_v1)

violin2.append(m1_v2)
violin2.append(m2_v2)
violin2.append(m3_v2)

violin3.append(m1_v3)
violin3.append(m2_v3)
violin3.append(m3_v3)

cello.append(m1_c)
cello.append(m2_c)
cello.append(m3_c)

# Add parts to score
s.insert(0, violin1)
s.insert(0, violin2)
s.insert(0, violin3)
s.insert(0, cello)

# Show in MuseScore
s.show()