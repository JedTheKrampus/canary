#!/usr/bin/env python
# encoding: utf-8
'''
canary.py
#   Created on Sun Aug 21 2011 11:01 GMT -0600 by Izzy Cecil & Fuzzo & Arctem
'''
'''
What hall is best?:
'West is best.'
(575)-323-0668
(575)-323-0NMT
PIN = 1928
'''
import os, sys
from traceback import print_exc
from googlevoice import Voice
import commands
import canarydata
from canary_util import Textcolors

EMAIL = 'nmtcanary@gmail.com'
PASSWORD = 'NewMexicoTech'
voice = Voice()

debug = False

def login():
    print 'Logging in to nmtcanary@gmail.com...'
    try:
        voice.login(EMAIL, PASSWORD)
        print 'Logged in as nmtcanary@gmail.com!'
    except:
        print 'Failed to login. Please make sure you are connected to the internet.'
        
    

def shell():
    while True:
        try:
            command = raw_input(Textcolors.PROMPT+'Canary> '+Textcolors.END)
            command = command.lower().split()
            if command[0] in ('quit','exit'):
                return
            if command[0] in ('ls','list'):
                print dir(commands)
                continue
            if command[0] in ('clear','cls'):
                os.system(['clear','cls'][os.name=='nt'])
                continue
            getattr(commands,command[0],commands.not_found)(voice, canarydata.phonebook, command)
        except (KeyboardInterrupt, SystemExit):
            print '\n'
            print Textcolors.FAIL+'\aProcess Cancelled'+Textcolors.END
            print 
        except:
            print Textcolors.FAIL+'\aAn Error Occured:'
            print_exc()
            print Textcolors.END

def main(argv):
    global debug
    if 'debug' in argv:
        debug = True
        print 'Entering debug mode.'
        argv.remove('debug')
    else:
        debug = False
    login()
    canarydata.load_phonebook(debug)
    if len(argv) is 0:
        print '''

                         _   _ __  __ _______ 
                        | \ | |  \/  |__   __|
                        |  \| | \  / |  | |   
                        | . ` | |\/| |  | |   
                        | |\  | |  | |  | |   
                        |_| \_|_|  |_|  |_|   
 __  __ _                 _        _____                             
|  \/  (_)               ( )      / ____|                            
| \  / |_ _ __   ___ _ __|/ ___  | |     __ _ _ __   __ _ _ __ _   _ 
| |\/| | | '_ \ / _ \ '__| / __| | |    / _` | '_ \ / _` | '__| | | |
| |  | | | | | |  __/ |    \__ \ | |___| (_| | | | | (_| | |  | |_| |
|_|  |_|_|_| |_|\___|_|    |___/  \_____\__,_|_| |_|\__,_|_|   \__, |
                                                                __/ |
Created by Spencer Brown, Tyler Cecil, and Russell White       |___/ 
'''
        shell()
        return 0
    print 'Only shell is active currently'
    print 'To activate, run "python canary.py" with no arguments'
    return -1

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
