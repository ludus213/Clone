from midiutil import MIDIFile
import os

def generate_main_theme():
    """
    Generates a more complex main theme with melody, chords, and bass.
    """
    track_melody = 0
    track_chords = 1
    track_bass = 2
    channel = 0
    time = 0
    duration_melody = 0.5
    duration_chord = 4
    duration_bass = 4
    tempo = 140
    volume_melody = 100
    volume_chords = 70
    volume_bass = 80

    MyMIDI = MIDIFile(3) # 3 tracks
    MyMIDI.addTempo(track_melody, time, tempo)
    MyMIDI.addTempo(track_chords, time, tempo)
    MyMIDI.addTempo(track_bass, time, tempo)

    # Chord progression: Cm - Bb - F - F
    chords = [
        [60, 63, 67], # Cm
        [58, 62, 65], # Bb
        [53, 57, 60], # F
        [53, 57, 60]  # F
    ]
    bass_notes = [48, 46, 41, 41] # C, Bb, F, F

    # Melody
    melody = [72, 75, 74, 72, 70, 72, 68, 70, 67, 68, 65, 67, 63, 65, 62, 63]

    for i in range(4): # Loop the progression 4 times
        # Chords
        MyMIDI.addNote(track_chords, channel, chords[i % 4][0], time + i * 4, duration_chord, volume_chords)
        MyMIDI.addNote(track_chords, channel, chords[i % 4][1], time + i * 4, duration_chord, volume_chords)
        MyMIDI.addNote(track_chords, channel, chords[i % 4][2], time + i * 4, duration_chord, volume_chords)
        # Bass
        MyMIDI.addNote(track_bass, channel, bass_notes[i % 4], time + i * 4, duration_bass, volume_bass)
        # Melody
        for j in range(16):
             MyMIDI.addNote(track_melody, channel, melody[j], time + i * 4 + j * 0.25, duration_melody, volume_melody)

    output_path = os.path.join("assets", "music", "main_theme.mid")
    with open(output_path, "wb") as output_file:
        MyMIDI.writeFile(output_file)
    print(f"Main theme saved to {output_path}")

def generate_menu_theme():
    """
    Generates a more ambient menu theme with arpeggiated chords.
    """
    track = 0
    channel = 0
    time = 0
    duration = 1
    tempo = 80
    volume = 90

    MyMIDI = MIDIFile(1)
    MyMIDI.addTempo(track, time, tempo)

    # Chord progression: Am - G - C - F
    chords = [
        [57, 60, 64], # Am
        [55, 59, 62], # G
        [60, 64, 67], # C
        [53, 57, 60]  # F
    ]

    for i in range(8): # Loop 8 times
        chord = chords[i % 4]
        # Arpeggiate the chord
        MyMIDI.addNote(track, channel, chord[0], time + i * 2, 0.5, volume)
        MyMIDI.addNote(track, channel, chord[1], time + i * 2 + 0.5, 0.5, volume)
        MyMIDI.addNote(track, channel, chord[2], time + i * 2 + 1, 0.5, volume)
        MyMIDI.addNote(track, channel, chord[1], time + i * 2 + 1.5, 0.5, volume)


    output_path = os.path.join("assets", "music", "menu_theme.mid")
    with open(output_path, "wb") as output_file:
        MyMIDI.writeFile(output_file)
    print(f"Menu theme saved to {output_path}")

if __name__ == "__main__":
    generate_main_theme()
    generate_menu_theme()
