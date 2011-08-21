# File: commands.py
#
# Contains the commands that the shell can call.

from googlevoice import Voice
from googlevoice.util import input
from student import Student


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
        while input('Would you like to add a filter? [y/N]: ').lower() in ('y'):
            add_filter(filters)
            print filters
        print 'DONE'
    else:
        print 'THIS IS WHERE THE COMAND ARGS SHOULD GO'

def add_filter(filters):
    filter_type = raw_input('What type of filter? : ')
    filter_type = filter_type.lower()
    if filter_type in ('hall'):
        halls = raw_input('Which halls?')
        halls = halls.lower().split()
        for hall in halls:
            if hall not in ('west','presidents','south','bacha','driscoll'):
                print 'Hall "%s" not found...' % (hall)
                print 'Filter not added...'
                return
        filters.append((filter_type,halls))
        return
    if filter_type in ('gender'):
        gender = raw_input('Male of Female? [m/F]: ')
        if gender.lower() not in ('m','f'):
            print 'Error...'
            print 'Type "m" for Male, or "f" for Female'
            return
        filters.append((filter_type,gender))
        return
    if filter_type in ('year'):
        years = raw_input('Which years? (only undergrad, number seperated by a space): ')
        years = years.split()
        for year in years:
            if year not in ('1','2','3','4','5','6'):
                print 'Error...'
                print '%s is not a valid number...' %(year)
                return
        filters.append((filter_type,years))
        return
    if filter_type in ('help','ls','list'):
        print 'Type eather "hall", "gender", or "year" to creat a filter of the apropreat type.'
        print 'Each will provide their own instructions for creating a filter.'
        return
    
                        
def help(phonebook,voice,args):
    print 'Welcome. It would apear you are fucked. Sucks to suck!'



<<<<<<< HEAD
def help():
    print """Canary detects that you don't know what you are doing.

Use the send command in the canary shell to send a mass text to the populace of
New Mexico Tech. To do this, start canary.py and type a command like this:

Canary> send "New Mexico Tech students: Meet in front of Presidents' Hall for an El Camino run."

Then press enter. Canary will proceed to send out your mass text to all the
students who have signed up to receive Canary text messages. Students may have
opted in to delay texts or not receive them at all at certain times of day."""
=======
    
>>>>>>> 131dbe49330794ac647f95b5c36d0fed16cb1092
