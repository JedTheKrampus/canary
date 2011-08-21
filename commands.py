# File: commands.py
#
# Contains the commands that the shell can call.

from googlevoice import Voice
from googlevoice.util import input

"""This default command is called when the command does not exist."""
def not_found(phonebook, voice, args):
    print "Command not found: " + args[0]

"""This command sends a text message to a subset of the students as defined by
the arguments. The last argument is the message, so you should enclose the
message in quotes.

Arguments before the message constitute subsets of the phonebook."""
def send(phonebook, voice, args):
    if len(args) == 0:
        help()

def help():
    print """Canary detects that you don't know what you are doing.

Use the send command in the canary shell to send a mass text to the populace of
New Mexico Tech. To do this, start canary.py and type a command like this:

Canary> send "New Mexico Tech students: Meet in front of Presidents' Hall for an El Camino run."

Then press enter. Canary will proceed to send out your mass text to all the
students who have signed up to receive Canary text messages. Students may have
opted in to delay texts or not receive them at all at certain times of day."""
