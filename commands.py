# File: commands.py
#
# Contains the commands that the shell can call.

from googlevoice import Voice
from student import Student
import canary_util



"""This default command is called when the command does not exist."""
def not_found(phonebook, voice, args):
    print "Command not found: " + args[0]

"""This command sends a text message to a subset of the students as defined by
the arguments. The last argument is the message, so you should enclose the
message in quotes.

Arguments before the message constitute subsets of the phonebook."""
def text(phonebook, voice, args):
    if len(args) == 0:
        filters = []
        text = raw_input('What would you like to send?\n')
        while input('Would you like to add a filter? [y/N]: ').lower() == 'y':
            canary_util.add_filter(filters)
        canary_util.show_text(text,filters)
    else:
        print 'THIS IS WHERE THE COMMAND ARGS SHOULD GO'
                            
def help(phonebook,voice,args):
    print 'Welcome. It would appear you are fucked. Sucks to suck!'

