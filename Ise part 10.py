from music21 import *

environment.set('musicxmlPath', r'C:\Program Files\MuseScore 4\bin\MuseScore4.exe')


def get_key_signature():
    print("Enter key signature.")
    print("Examples:")
    print("  G major")
    print("  D major")
    print("  E minor")
    print("  B-flat major")

    key_input = input("Key: ").strip()
    k = key.Key(key_input)
    return k


def get_instrument_object(name):
    """Turn a typed instrument name into a music21 instrument object."""
    name = name.strip().lower()

    instrument_map = {
        "violin": instrument.Violin(),
        "violin 1": instrument.Violin(),
        "violin 2": instrument.Violin(),
        "violin 3": instrument.Violin(),
        "cello": instrument.Violoncello(),
        "violoncello": instrument.Violoncello(),
        "viola": instrument.Viola(),
        "flute": instrument.Flute(),
        "oboe": instrument.Oboe(),
        "clarinet": instrument.Clarinet(),
        "bassoon": instrument.Bassoon(),
        "trumpet": instrument.Trumpet(),
        "horn": instrument.Horn(),
        "trombone": instrument.Trombone(),
        "tuba": instrument.Tuba(),
        "piano": instrument.Piano(),
        "soprano": instrument.Soprano(),
        "alto": instrument.Alto(),
        "tenor": instrument.Tenor(),
        "bass": instrument.Bass(),
        "guitar": instrument.Guitar(),
    }

    if name in instrument_map:
        inst = instrument_map[name]
    else:
        inst = instrument.Instrument()
        inst.partName = name.title()
        inst.instrumentName = name.title()

    return inst


def choose_clef(inst_name):
    """Basic clef choice based on instrument name."""
    name = inst_name.lower()
    if "cello" in name or "violoncello" in name or "bass" in name or "tuba" in name or "trombone" in name or "bassoon" in name:
        return clef.BassClef()
    elif "viola" in name:
        return clef.AltoClef()
    else:
        return clef.TrebleClef()


def create_measure_from_input(measure_number):
    """
    Ask user for notes/rests for one measure.
    Format:
      note C4 0.5
      rest 1.5
    Type 'done' when finished.
    """
    m = stream.Measure(number=measure_number)

    print(f"\nEntering contents for measure {measure_number}")
    print("Enter one item at a time in one of these formats:")
    print("  note C4 0.5")
    print("  note F#4 1.5")
    print("  rest 0.5")
    print("Type 'done' when finished with this measure.")

    total_length = 0.0

    while True:
        user_input = input("Item: ").strip()

        if user_input.lower() == "done":
            break

        parts = user_input.split()
        if len(parts) < 2:
            print("Invalid input. Try again.")
            continue

        kind = parts[0].lower()

        try:
            if kind == "note" and len(parts) == 3:
                pitch_name = parts[1]
                ql = float(parts[2])
                n = note.Note(pitch_name, quarterLength=ql)
                m.append(n)
                total_length += ql

            elif kind == "rest" and len(parts) == 2:
                ql = float(parts[1])
                r = note.Rest(quarterLength=ql)
                m.append(r)
                total_length += ql

            else:
                print("Invalid format. Use 'note C4 0.5' or 'rest 1.5'")
                continue

        except Exception as e:
            print("Error:", e)

    print(f"Total quarterLength entered in measure {measure_number}: {total_length}")
    return m


def build_score():
    s = stream.Score()

    # Metadata
    title = input("Name of piece: ").strip()
    composer_name = input("Composer: ").strip()
    time_sig = input("Time signature (e.g. 9/8, 4/4, 3/4): ").strip()
    tempo_bpm = int(input("Tempo number (e.g. 68, 120): ").strip())

    print("\nTempo beat unit examples:")
    print("quarter = crotchet")
    print("eighth = quaver")
    print("half = minim")
    print("For dotted crotchet in 9/8, type: dotted-quarter")
    tempo_unit = input("Tempo beat unit (quarter, eighth, half, dotted-quarter): ").strip().lower()

    k = get_key_signature()

    # Metadata
    s.metadata = metadata.Metadata()
    s.metadata.title = title
    s.metadata.composer = composer_name

    # Tempo referent
    if tempo_unit == "quarter":
        referent = duration.Duration(1.0)
    elif tempo_unit == "eighth":
        referent = duration.Duration(0.5)
    elif tempo_unit == "half":
        referent = duration.Duration(2.0)
    elif tempo_unit == "dotted-quarter":
        referent = duration.Duration(1.5)
    else:
        print("Unknown tempo unit, defaulting to quarter.")
        referent = duration.Duration(1.0)

    tempo_mark = tempo.MetronomeMark(number=tempo_bpm, referent=referent)

    # Instruments
    num_instruments = int(input("\nHow many instruments/parts? ").strip())
    num_measures = int(input("How many measures? ").strip())

    parts_list = []

    for i in range(num_instruments):
        inst_name = input(f"\nEnter name of instrument/part {i+1}: ").strip()

        p = stream.Part()
        inst = get_instrument_object(inst_name)
        p.insert(0, inst)

        # Make names appear nicely
        p.partName = inst_name
        p.partAbbreviation = inst_name

        # First measure gets setup info
        for measure_number in range(1, num_measures + 1):
            m = create_measure_from_input(measure_number)

            if measure_number == 1:
                m.insert(0, choose_clef(inst_name))
                m.insert(0, key.KeySignature(k.sharps))
                m.insert(0, meter.TimeSignature(time_sig))
                if i == 0:
                    m.insert(0, tempo_mark)

            p.append(m)

        parts_list.append(p)

    # Add all parts to score
    for p in parts_list:
        s.insert(0, p)

    return s


def main():
    score = build_score()

    print("\nScore created.")
    save_xml = input("Save as MusicXML as well? (yes/no): ").strip().lower()

    if save_xml == "yes":
        filename = input("Filename (without extension): ").strip()
        score.write('musicxml', fp=f"{filename}.musicxml")
        print(f"Saved as {filename}.musicxml")

    score.show()


if __name__ == "__main__":
    main()