import winsound
import msvcrt
import keyboard
import random

print ("Copyright (c) 2020 by Lexzach")
print ("Thank you for using this software!")
print ("")
print ("-=-THIS WINDOW MUST STAY OPENED FOR KEYBOARD SOUNDS TO PLAY!-=-")
print ("--- You can minimize this window, just don't close it ---")
while True:
    if keyboard.read_key() != "space":
        numgen = random.randint(0,3)
        pressvar = "press" + str(numgen) + ".wav"
        keystroke = keyboard.read_key()
        winsound.PlaySound(pressvar, winsound.SND_ASYNC)
    elif keyboard.read_key() =="space":
        winsound.PlaySound("spacebar.wav", winsound.SND_ASYNC)