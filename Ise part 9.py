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
# BAR 4
# =========================

m4_v1 = stream.Measure(number=4)
m4_v2 = stream.Measure(number=4)
m4_v3 = stream.Measure(number=4)
m4_c = stream.Measure(number=4)

# Violin 1
m4_v1.append(note.Note("F#4", quarterLength=0.5))
m4_v1.append(note.Note("G4", quarterLength=0.5))
m4_v1.append(note.Note("A4", quarterLength=0.5))
m4_v1.append(note.Note("D4", quarterLength=0.5))
m4_v1.append(note.Note("F#4", quarterLength=0.5))
m4_v1.append(note.Note("A4", quarterLength=0.5))
m4_v1.append(note.Note("C4", quarterLength=0.5))
m4_v1.append(note.Note("B4", quarterLength=0.5))
m4_v1.append(note.Note("A4", quarterLength=0.5))

# Violin 2
m4_v2.append(note.Note("A3", quarterLength=1))
m4_v2.append(note.Note("D4", quarterLength=0.5))
m4_v2.append(note.Note("A4", quarterLength=1))
m4_v2.append(note.Note("G4", quarterLength=0.5))
m4_v2.append(note.Note("A4", quarterLength=1))
m4_v2.append(note.Note("F#4", quarterLength=0.5))

# Violin 3
m4_v3.append(note.Note("D4", quarterLength=1.5))
m4_v3.append(note.Note("D4", quarterLength=1.5))
m4_v3.append(note.Note("D4", quarterLength=1.5))

# Cello
m4_c.append(note.Note("D3", quarterLength=1.5))
m4_c.append(note.Note("F#3", quarterLength=1.5))
m4_c.append(note.Note("D3", quarterLength=1.5))

# =========================
# BAR 5
# =========================

m5_v1 = stream.Measure(number=5)
m5_v2 = stream.Measure(number=5)
m5_v3 = stream.Measure(number=5)
m5_c = stream.Measure(number=5)

# Violin 1
m5_v1.append(note.Note("B4", quarterLength=0.5))
m5_v1.append(note.Note("G4", quarterLength=0.5))
m5_v1.append(note.Note("A4", quarterLength=0.5))
m5_v1.append(note.Note("B4", quarterLength=0.5))
m5_v1.append(note.Note("D5", quarterLength=0.5))
m5_v1.append(note.Note("C5", quarterLength=0.5))
m5_v1.append(note.Note("C5", quarterLength=0.5))
m5_v1.append(note.Note("E5", quarterLength=0.5))
m5_v1.append(note.Note("D5", quarterLength=0.5))

# Violin 2
m5_v2.append(note.Note("D4", quarterLength=1))
m5_v2.append(note.Note("F#4", quarterLength=0.5))
m5_v2.append(note.Note("G4", quarterLength=1))
m5_v2.append(note.Note("F#4", quarterLength=0.5))
m5_v2.append(note.Note("G4", quarterLength=1))
m5_v2.append(note.Note("A4", quarterLength=0.5))

# Violin 3
m5_v3.append(note.Note("G4", quarterLength=1.5))
m5_v3.append(note.Note("E4", quarterLength=1.5))
m5_v3.append(note.Note("E4", quarterLength=1.5))

# Cello
m5_c.append(note.Note("G3", quarterLength=1.5))
m5_c.append(note.Note("E3", quarterLength=1.5))
m5_c.append(note.Note("C3", quarterLength=1.5))

# =========================
# BAR 6
# =========================

m6_v1 = stream.Measure(number=6)
m6_v2 = stream.Measure(number=6)
m6_v3 = stream.Measure(number=6)
m6_c = stream.Measure(number=6)

# Violin 1
m6_v1.append(note.Note("D5", quarterLength=0.5))
m6_v1.append(note.Note("G5", quarterLength=0.5))
m6_v1.append(note.Note("F#5", quarterLength=0.5))
m6_v1.append(note.Note("G5", quarterLength=0.5))
m6_v1.append(note.Note("D5", quarterLength=0.5))
m6_v1.append(note.Note("B4", quarterLength=0.5))
m6_v1.append(note.Note("G4", quarterLength=0.5))
m6_v1.append(note.Note("A4", quarterLength=0.5))
m6_v1.append(note.Note("B4", quarterLength=0.5))

# Violin 2
m6_v2.append(note.Note("B4", quarterLength=1))
m6_v2.append(note.Note("A4", quarterLength=0.5))
m6_v2.append(note.Note("B4", quarterLength=1))
m6_v2.append(note.Note("G4", quarterLength=0.5))
m6_v2.append(note.Note("E4", quarterLength=1))
m6_v2.append(note.Note("G4", quarterLength=0.5))

# Violin 3
m6_v3.append(note.Note("G4", quarterLength=1))
m6_v3.append(note.Note("F#4", quarterLength=0.5))
m6_v3.append(note.Note("E4", quarterLength=1.5))
m6_v3.append(note.Note("D4", quarterLength=1.5))

# Cello
m6_c.append(note.Note("B2", quarterLength=1.5))
m6_c.append(note.Note("E3", quarterLength=1.5))
m6_c.append(note.Note("D3", quarterLength=1.5))

# =========================
# BAR 7
# =========================

m7_v1 = stream.Measure(number=7)
m7_v2 = stream.Measure(number=7)
m7_v3 = stream.Measure(number=7)
m7_c = stream.Measure(number=7)

# Violin 1
m7_v1.append(note.Note("E4", quarterLength=0.5))
m7_v1.append(note.Note("D5", quarterLength=0.5))
m7_v1.append(note.Note("C5", quarterLength=0.5))
m7_v1.append(note.Note("B4", quarterLength=0.5))
m7_v1.append(note.Note("A4", quarterLength=0.5))
m7_v1.append(note.Note("G4", quarterLength=0.5))
m7_v1.append(note.Note("D4", quarterLength=0.5))
m7_v1.append(note.Note("G4", quarterLength=0.5))
m7_v1.append(note.Note("F#4", quarterLength=0.5))

# Violin 2
m7_v2.append(note.Note("A4", quarterLength=1))
m7_v2.append(note.Note("F#4", quarterLength=0.5))
m7_v2.append(note.Note("G4", quarterLength=1))
m7_v2.append(note.Note("E4", quarterLength=0.5))
m7_v2.append(note.Note("A3", quarterLength=1))
m7_v2.append(note.Note("C4", quarterLength=0.5))

# Violin 3
m7_v3.append(note.Note("D4", quarterLength=1.5))
m7_v3.append(note.Note("E4", quarterLength=1.5))
m7_v3.append(note.Note("D4", quarterLength=1.5))

# Cello
m7_c.append(note.Note("C3", quarterLength=1.5))
m7_c.append(note.Note("C#3", quarterLength=1.5))
m7_c.append(note.Note("D3", quarterLength=1.5))

# =========================
# BAR 8
# =========================

m8_v1 = stream.Measure(number=8)
m8_v2 = stream.Measure(number=8)
m8_v3 = stream.Measure(number=8)
m8_c = stream.Measure(number=8)

# Violin 1
m8_v1.append(note.Note("G4", quarterLength=0.5))
m8_v1.append(note.Note("B4", quarterLength=0.5))
m8_v1.append(note.Note("D5", quarterLength=0.5))
m8_v1.append(note.Note("G5", quarterLength=0.5))
m8_v1.append(note.Note("D5", quarterLength=0.5))
m8_v1.append(note.Note("B4", quarterLength=0.5))
m8_v1.append(note.Note("G4", quarterLength=0.5))
m8_v1.append(note.Note("B4", quarterLength=0.5))
m8_v1.append(note.Note("D5", quarterLength=0.5))

# Violin 2
m8_v2.append(note.Note("B3", quarterLength=1))
m8_v2.append(note.Note("G4", quarterLength=0.5))
m8_v2.append(note.Note("B4", quarterLength=1))
m8_v2.append(note.Note("D5", quarterLength=0.5))
m8_v2.append(note.Note("G5", quarterLength=1.5))

# Violin 3
m8_v3.append(note.Note("G3", quarterLength=1.5))
m8_v3.append(note.Rest(quarterLength=2))
m8_v3.append(note.Rest(quarterLength=1))

# Cello
m8_c.append(note.Note("G2", quarterLength=1.5))
m8_c.append(note.Rest(quarterLength=1))
m8_c.append(note.Note("G3", quarterLength=0.5))
m8_c.append(note.Note("D3", quarterLength=1))
m8_c.append(note.Note("B2", quarterLength=0.5))

# =========================
# BAR 9
# =========================

m9_v1 = stream.Measure(number=9)
m9_v2 = stream.Measure(number=9)
m9_v3 = stream.Measure(number=9)
m9_c = stream.Measure(number=9)

# Violin 1
m9_v1.append(note.Note("G5", quarterLength=2))
m9_v1.append(note.Rest(quarterLength=1))
m9_v1.append(note.Note("C5", quarterLength=1.5))

# Violin 2
m9_v2.append(note.Note("G4", quarterLength=3))
m9_v2.append(note.Note("G4", quarterLength=1.5))

# Violin 3
m9_v3.append(note.Note("D4", quarterLength=3))
m9_v3.append(note.Note("E4", quarterLength=1.5))

# Cello
m9_c.append(note.Note("G2", quarterLength=1.5))
m9_c.append(note.Note("F#3", quarterLength=1.5))
m9_c.append(note.Note("E3", quarterLength=1.5))

# =========================
# BAR 10
# =========================

m10_v1 = stream.Measure(number=10)
m10_v2 = stream.Measure(number=10)
m10_v3 = stream.Measure(number=10)
m10_c = stream.Measure(number=10)

# Violin 1
m10_v1.append(note.Note("D5", quarterLength=3))
m10_v1.append(note.Note("D5", quarterLength=1.5))

# Violin 2
m10_v2.append(note.Note("A4", quarterLength=1.5))
m10_v2.append(note.Note("G4", quarterLength=1.5))
m10_v2.append(note.Note("F#4", quarterLength=1.5))

# Violin 3
m10_v3.append(note.Note("A3", quarterLength=3))
m10_v3.append(note.Note("B3", quarterLength=1.5))


# Cello
m10_c.append(note.Note("F#3", quarterLength=1.5))
m10_c.append(note.Note("E3", quarterLength=1.5))
m10_c.append(note.Note("D3", quarterLength=1.5))

# =========================
# BAR 11
# =========================

m11_v1 = stream.Measure(number=11)
m11_v2 = stream.Measure(number=11)
m11_v3 = stream.Measure(number=11)
m11_c = stream.Measure(number=11)

# Violin 1
m11_v1.append(note.Note("C5", quarterLength=3))
m11_v1.append(note.Note("B4", quarterLength=1.5))

# Violin 2
m11_v2.append(note.Note("G4", quarterLength=1.5))
m11_v2.append(note.Note("D4", quarterLength=3))

# Violin 3
m11_v3.append(note.Note("B3", quarterLength=1.5))
m11_v3.append(note.Note("A3", quarterLength=1.5))
m11_v3.append(note.Note("G3", quarterLength=1.5))

# Cello
m11_c.append(note.Note("E3", quarterLength=1.5))
m11_c.append(note.Note("F#3", quarterLength=1.5))
m11_c.append(note.Note("G3", quarterLength=1.5))

# =========================
# BAR 12
# =========================

m12_v1 = stream.Measure(number=12)
m12_v2 = stream.Measure(number=12)
m12_v3 = stream.Measure(number=12)
m12_c = stream.Measure(number=12)

# Violin 1
m12_v1.append(note.Rest(quarterLength=0.5))
m12_v1.append(note.Note("D4", quarterLength=0.5))
m12_v1.append(note.Note("E4", quarterLength=0.5))
m12_v1.append(note.Note("F#4", quarterLength=0.5))
m12_v1.append(note.Note("A4", quarterLength=0.5))
m12_v1.append(note.Note("G4", quarterLength=0.5))
m12_v1.append(note.Note("A4", quarterLength=0.5))
m12_v1.append(note.Note("C5", quarterLength=0.5))
m12_v1.append(note.Note("B4", quarterLength=0.5))

# Violin 2
m12_v2.append(note.Note("D4", quarterLength=1.5))
m12_v2.append(note.Note("D4", quarterLength=1.5))
m12_v2.append(note.Note("F#4", quarterLength=1))
m12_v2.append(note.Note("G4", quarterLength=0.5))

# Violin 3
m12_v3.append(note.Note("A3", quarterLength=1.5))
m12_v3.append(note.Note("A3", quarterLength=1.5))
m12_v3.append(note.Rest(quarterLength=1))
m12_v3.append(note.Rest(quarterLength=0.5))

# Cello
m12_c.append(note.Note("D3", quarterLength=1.5))
m12_c.append(note.Rest(quarterLength=1))
m12_c.append(note.Note("D3", quarterLength=0.5))
m12_c.append(note.Note("D3", quarterLength=1))
m12_c.append(note.Note("D3", quarterLength=0.5))

# =========================
# BAR 13
# =========================

m13_v1 = stream.Measure(number=13)
m13_v2 = stream.Measure(number=13)
m13_v3 = stream.Measure(number=13)
m13_c = stream.Measure(number=13)

# Violin 1
m13_v1.append(note.Note("C5", quarterLength=0.5))
m13_v1.append(note.Note("A4", quarterLength=0.5))
m13_v1.append(note.Note("F#4", quarterLength=0.5))
m13_v1.append(note.Note("D4", quarterLength=0.5))
m13_v1.append(note.Note("F#4", quarterLength=0.5))
m13_v1.append(note.Note("A4", quarterLength=0.5))
m13_v1.append(note.Note("C5", quarterLength=0.5))
m13_v1.append(note.Note("B4", quarterLength=0.5))
m13_v1.append(note.Note("A4", quarterLength=0.5))

# Violin 2
m13_v2.append(note.Note("A4", quarterLength=1))
m13_v2.append(note.Note("C5", quarterLength=0.5))
m13_v2.append(note.Note("A4", quarterLength=1))
m13_v2.append(note.Note("F#4", quarterLength=0.5))
m13_v2.append(note.Note("D4", quarterLength=1))
m13_v2.append(note.Note("F#4", quarterLength=0.5))

# Violin 3
m13_v3.append(note.Rest(quarterLength=4.5))

# Cello
m13_c.append(note.Note("D2", quarterLength=1.5))
m13_c.append(note.Rest(quarterLength=1))
m13_c.append(note.Note("D3", quarterLength=0.5))
m13_c.append(note.Note("D3", quarterLength=1))
m13_c.append(note.Note("D3", quarterLength=0.5))

# =========================
# BAR 14
# =========================

m14_v1 = stream.Measure(number=14)
m14_v2 = stream.Measure(number=14)
m14_v3 = stream.Measure(number=14)
m14_c = stream.Measure(number=14)

# Violin 1
m14_v1.append(note.Note("B4", quarterLength=0.5))
m14_v1.append(note.Note("G4", quarterLength=0.5))
m14_v1.append(note.Note("A4", quarterLength=0.5))
m14_v1.append(note.Note("B4", quarterLength=0.5))
m14_v1.append(note.Note("D5", quarterLength=0.5))
m14_v1.append(note.Note("C5", quarterLength=0.5))
m14_v1.append(note.Note("C5", quarterLength=0.5))
m14_v1.append(note.Note("E5", quarterLength=0.5))
m14_v1.append(note.Note("D5", quarterLength=0.5))

# Violin 2
m14_v2.append(note.Note("B4", quarterLength=3))
m14_v2.append(note.Note("C5", quarterLength=1.5))

# Violin 3
m14_v3.append(note.Note("G4", quarterLength=3))
m14_v3.append(note.Note("G4", quarterLength=1.5))

# Cello
m14_c.append(note.Note("G3", quarterLength=1.5))
m14_c.append(note.Note("F#3", quarterLength=1.5))
m14_c.append(note.Note("E3", quarterLength=1.5))

# =========================
# BAR 15
# =========================

m15_v1 = stream.Measure(number=15)
m15_v2 = stream.Measure(number=15)
m15_v3 = stream.Measure(number=15)
m15_c = stream.Measure(number=15)

# Violin 1
m15_v1.append(note.Note("D5", quarterLength=0.5))
m15_v1.append(note.Note("G5", quarterLength=0.5))
m15_v1.append(note.Note("F#5", quarterLength=0.5))
m15_v1.append(note.Note("G5", quarterLength=0.5))
m15_v1.append(note.Note("D5", quarterLength=0.5))
m15_v1.append(note.Note("B4", quarterLength=0.5))
m15_v1.append(note.Note("G4", quarterLength=0.5))
m15_v1.append(note.Note("A4", quarterLength=0.5))
m15_v1.append(note.Note("B4", quarterLength=0.5))

# Violin 2
m15_v2.append(note.Note("D5", quarterLength=1.5))
m15_v2.append(note.Note("G4", quarterLength=1.5))
m15_v2.append(note.Note("B4", quarterLength=1.5))

# Violin 3
m15_v3.append(note.Note("G4", quarterLength=1.5))
m15_v3.append(note.Note("D4", quarterLength=1.5))
m15_v3.append(note.Note("G4", quarterLength=1.5))

# Cello
m15_c.append(note.Note("B3", quarterLength=1.5))
m15_c.append(note.Note("B2", quarterLength=1.5))
m15_c.append(note.Note("E3", quarterLength=1.5))

# =========================
# BAR 16
# =========================

m16_v1 = stream.Measure(number=16)
m16_v2 = stream.Measure(number=16)
m16_v3 = stream.Measure(number=16)
m16_c = stream.Measure(number=16)

# Violin 1
m16_v1.append(note.Note("E4", quarterLength=0.5))
m16_v1.append(note.Note("D5", quarterLength=0.5))
m16_v1.append(note.Note("C5", quarterLength=0.5))
m16_v1.append(note.Note("B4", quarterLength=0.5))
m16_v1.append(note.Note("A4", quarterLength=0.5))
m16_v1.append(note.Note("G4", quarterLength=0.5))
m16_v1.append(note.Note("D4", quarterLength=0.5))
m16_v1.append(note.Note("G4", quarterLength=0.5))
m16_v1.append(note.Note("F#4", quarterLength=0.5))

# Violin 2
m16_v2.append(note.Note("A4", quarterLength=1))
m16_v2.append(note.Note("B4", quarterLength=0.25))
m16_v2.append(note.Note("C5", quarterLength=0.25))
m16_v2.append(note.Note("B4", quarterLength=1.5))
m16_v2.append(note.Note("A4", quarterLength=1.5))

# Violin 3
m16_v3.append(note.Note("E4", quarterLength=1.5))
m16_v3.append(note.Note("E4", quarterLength=0.5))
m16_v3.append(note.Note("F#4", quarterLength=0.5))
m16_v3.append(note.Note("E4", quarterLength=0.5))
m16_v3.append(note.Note("F#4", quarterLength=1.5))

# Cello
m16_c.append(note.Note("C3", quarterLength=1.5))
m16_c.append(note.Note("D3", quarterLength=1.5))
m16_c.append(note.Note("D2", quarterLength=1.5))

# =========================
# BAR 17
# =========================

m17_v1 = stream.Measure(number=17)
m17_v2 = stream.Measure(number=17)
m17_v3 = stream.Measure(number=17)
m17_c = stream.Measure(number=17)

# Violin 1
m17_v1.append(note.Note("G4", quarterLength=3))
m17_v1.append(note.Rest(quarterLength=1.5))

# Violin 2
m17_v2.append(note.Note("G4", quarterLength=3))
m17_v2.append(note.Rest(quarterLength=1.5))

# Violin 3
m17_v3.append(note.Note("D4", quarterLength=3))
m17_v3.append(note.Rest(quarterLength=1.5))

# Cello
m17_c.append(note.Note("G2", quarterLength=3))
m17_c.append(note.Rest(quarterLength=1.5))

# =========================
# ADD MEASURES TO PARTS
# =========================

violin1.append(m1_v1)
violin1.append(m2_v1)
violin1.append(m3_v1)
violin1.append(m4_v1)
violin1.append(m5_v1)
violin1.append(m6_v1)
violin1.append(m7_v1)
violin1.append(m8_v1)
violin1.append(m9_v1)
violin1.append(m10_v1)
violin1.append(m11_v1)
violin1.append(m12_v1)
violin1.append(m13_v1)
violin1.append(m14_v1)
violin1.append(m15_v1)
violin1.append(m16_v1)
violin1.append(m17_v1)

violin2.append(m1_v2)
violin2.append(m2_v2)
violin2.append(m3_v2)
violin2.append(m4_v2)
violin2.append(m5_v2)
violin2.append(m6_v2)
violin2.append(m7_v2)
violin2.append(m8_v2)
violin2.append(m9_v2)
violin2.append(m10_v2)
violin2.append(m11_v2)
violin2.append(m12_v2)
violin2.append(m13_v2)
violin2.append(m14_v2)
violin2.append(m15_v2)
violin2.append(m16_v2)
violin2.append(m17_v2)

violin3.append(m1_v3)
violin3.append(m2_v3)
violin3.append(m3_v3)
violin3.append(m4_v3)
violin3.append(m5_v3)
violin3.append(m6_v3)
violin3.append(m7_v3)
violin3.append(m8_v3)
violin3.append(m9_v3)
violin3.append(m10_v3)
violin3.append(m11_v3)
violin3.append(m12_v3)
violin3.append(m13_v3)
violin3.append(m14_v3)
violin3.append(m15_v3)
violin3.append(m16_v3)
violin3.append(m17_v3)

cello.append(m1_c)
cello.append(m2_c)
cello.append(m3_c)
cello.append(m4_c)
cello.append(m5_c)
cello.append(m6_c)
cello.append(m7_c)
cello.append(m8_c)
cello.append(m9_c)
cello.append(m10_c)
cello.append(m11_c)
cello.append(m12_c)
cello.append(m13_c)
cello.append(m14_c)
cello.append(m15_c)
cello.append(m16_c)
cello.append(m17_c)

# Add parts to score
s.insert(0, violin1)
s.insert(0, violin2)
s.insert(0, violin3)
s.insert(0, cello)

# Show in MuseScore
s.show()