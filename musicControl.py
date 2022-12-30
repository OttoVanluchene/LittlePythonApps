import keyboard

def playPause():
    # Press the play/pause media key to play or pause the music
    keyboard.send('play/pause')

def nextSong():
    # Press the next media key to play the next song
    keyboard.send('next track')

# Register the callback functions to listen for key press events
keyboard.add_hotkey('ctrl+num_1', playPause)
keyboard.add_hotkey('ctrl+num_2', nextSong)

# Run the event loop to listen for key press events
keyboard.wait()