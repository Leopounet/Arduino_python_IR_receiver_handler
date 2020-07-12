'''
You need to install pyserial to run this program.
To do so run the command: pip install pyserial.

All the code is mine and free to use under the MIT license.
'''
import serial, sys
import subprocess
from KeysHandler import KeysHandler, KeyNames

# Default port to use, you might have a different one, check that in your
# arduino IDE: tools > Port
port = "/dev/ttyACM0"

# This the baudrate at which you check inputs, should be the same as the one
# set in the .ino file
baudrate = "9600"

# For this simple example, this will control the output sound of your computer,
# and this is the delta value (+/- this percentage)
#
# Note: I didn't test the code on all version of Linux, so it might not work for
# you. I'm using Ubuntu 20.04, if it doesn't work, try doing something else, such
# as printing some text (which I already do technically)
rate = "1%"

# This object is used to hide the awful enumeration hidden behind this module
keysHandler = KeysHandler()

# You can give as argument the port and baudrate to use, faster if you just want
# to test the program
if len(sys.argv) == 3:
    port = sys.argv[1]
    baudrate = sys.argv[2]

# Simple method that increases the master volume of your computer
def increase_vol():
    command = "amixer -D pulse sset Master " + rate + "+"
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    process.communicate()
    print("Volume increased!")

# Simple method that decreases the master volume of your computer
def decrease_volume():
    command = "amixer -D pulse sset Master " + rate + "-"
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    process.communicate()
    print("Volume decreased!")

# Ugly but simple method that checks what key has been pressed and the executes
# the corresponding method
#
# Note: You may be intrigued by the "repeat" if. For some reason, when you hold
# down a button, it doesn't send the code for the button multiple times, it
# instead sends a special message, that stands for "a key is still pressed",
# equivalent to "the previous key is repeated".
def handle_key(keysHandler, key):
    if key == KeyNames.VOL_UP:
        increase_vol()

    elif key == KeyNames.VOL_DOWN:
        decrease_volume()

    elif key == KeyNames.REPEAT and keysHandler.last_key != keysHandler.invalid:
        handle_key(keysHandler, keysHandler.last_key)

# Gets the key that has been pressed and sends it to the key handler
def handle_sig(keysHandler, sig):
    key = keysHandler.getKeyFromCode(sig)
    if key != None:
        handle_key(keysHandler, key)

    if key != "repeat":
        keysHandler.last_key = key

# This method checks if a IR signal has been received. It reads the serial
# written by the arduino
def read(keysHandler, port, baudrate):
    with serial.Serial(port=port, baudrate=baudrate) as ser:
        while ser.isOpen():
            irsig = ser.readline().decode("utf-8").strip('\n\r')
            handle_sig(keysHandler, irsig)

read(keysHandler, port, baudrate)
