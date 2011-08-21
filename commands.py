# File: commands.py
#
# Contains the commands that the shell can call.

from googlevoice import Voice
from googlevoice.util import input

"""This default command is called when the command does not exist."""
def not_found(phonebook, voice, args):
    print "Command not found: " + args[0]
