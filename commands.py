'''
commands.py
# Contains the commands that the shell can call.
'''

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

"""This command adds a student to the phonebook."""
def add(phonebook, voice, args):
    name = raw_input(canary_util.Textcolors.OKBLUE+"What is the student's name?")

    number = raw_input(canary_util.Textcolors.OKBLUE+"What is the student's phone number? ")

    gender = raw_input(canary_util.Textcolors.OKBLUE+"What is the student's gender? [M/f] ")
    if gender.lower() in ("f", "female"):
        gender = "f"
    elif gender.lower() in ("m", "male"):
        gender = "m"
    else:
        print canary_util.Textcolors.WARNING+"Gender not found. Assuming male."
        gender = "m"

    year = raw_input(canary_util.Textcolors.OKBLUE+"What is the student's year in college? ")
    if year.lower().strip() in ("1", "1st", "1st-year", "1st year", "one", "first", "first-year", "first year", "freshman", "freshman year", "freshperson", "fish", "frosh", "new-g", "freshie", "fresher", "newbie", "newb", "noob", "n00b", "fresh-meat", "fresh meat", "rookie", "snotter", "bejant", "fledgling"):
        year = "1"
    elif year.lower().strip() in ("2", "2nd", "2nd-year", "2nd year", "two", "second", "second-year", "second year", "sophomore", "sophomore year", "semi-bejant"):
        year = "2"
    elif year.lower().strip() in ("3", "3rd", "3rd-year", "3rd year", "three", "third", "third-year", "third year", "junior", "junior year", "tertian"):
        year = "3"
    elif year.lower().strip() in ("4", "4th", "4th-year", "4th year", "four", "fourth", "fourth-year", "fourth year", "senior", "senior year", "magistrand"):
        year = "4"
    elif year.lower().strip() in ("5", "5th", "5th-year", "5th year", "five", "fifth", "fifth-year", "fifth year", "super-senior", "super senior", "supersenior", "victory lap"):
        year = "5"
    elif year.lower().strip() in ("6", "6th", "6th-year", "6th year", "six", "sixth", "sixth-year", "sixth year", "uber-senior", "uber senior", "ubersenior"):
        year = "6"
    else:
        print canary_util.Textcolors.FAIL+"Year not found. Aborting. (Undergraduates only, up to six years.) "
        return
    hall = raw_input(canary_util.Textcolors.OKBLUE+"In what hall does the student live? ")
    if hall.lower().strip() in ("presidents", "president's", "presidents'"):
        hall = "presidents"
    elif hall.lower().strip() in ("west", "south", "driscoll", "baca"):
        hall = hall.lower().strip()
    else:
        print canary_util.Textcolors.FAIL+"Hall not found. Aborting. (Residence halls only.) "
        return
    roomnum = int(raw_input(canary_util.Textcolors.OKBLUE+"What is the number of the student's room? ").strip())
    
    clubs = raw_input(canary_util.Textcolors.OKBLUE+"What clubs does the student belong to? (separate clubs with commas) ").split(",")
    for i in xrange(len(clubs)):
        clubs[i] = clubs[i].lower.strip()
    
    major = raw_input(canary_util.Textcolors.OKBLUE+"What major or majors is the student pursuing? ").split(",")
    for i in xrange(len(major)):
        major[i] = major[i].lower.strip()

    minor = raw_input(canary_util.Textcolors.OKBLUE+"What minor or minors is the student pursuing? ").split(",")
    for i in xrange(len(minor)):
        minor[i] = minor[i].lower.strip()

    canarydata.add_student(Student(name, number, gender, year, hall, roomnum, clubs, major, minor))
                            
def help(phonebook,voice,args):
    print canary_util.Textcolors.OKBLUE+'Welcome. It would appear you are fucked. Sucks to suck!'

