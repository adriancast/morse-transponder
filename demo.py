#!/usr/bin/env python3
# Import playsound module
from playsound import playsound

# Input an existing wav filename
wavFile = input("Enter a wav filename: ")
# Play the wav file
playsound(wavFile)

# Input an existing mp3 filename
mp3File = input("Enter a mp3 filename: ")
# Play the mp3 file
playsound(mp3File)