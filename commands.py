# File: commands.py
#
# Contains the commands that the shell can call.

from googlevoice import Voice
from student import Student
import canary_util



"""This default command is called when the command does not exist."""
def not_found(phonebook, voice, args):
    print canary_util.Textcolors.FAIL + 'Command not found: ' + args[0] + canary_util.Textcolors.END

"""This command sends a text message to a subset of the students as defined by
the arguments. The last argument is the message, so you should enclose the
message in quotes.

Arguments before the message constitute subsets of the phonebook."""
def text(phonebook, voice, args):
    if len(args) == 1:
        filters = []
        text = raw_input(canary_util.Textcolors.OKBLUE+'What would you like to send?\n'+canary_util.Textcolors.END)
        while raw_input(canary_util.Textcolors.OKBLUE+'Would you like to add a filter? [y/N]: '+canary_util.Textcolors.END).lower() == 'y':
            canary_util.add_filter(filters)
        canary_util.show_text(text,filters)
        
    else:
        print 'THIS IS WHERE THE COMMAND ARGS SHOULD GO'
                            
def help(phonebook,voice,args):
    print 'Welcome. It would appear you are fucked. Sucks to suck!'

