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
from googlevoice import Voice
import commands
import canarydata

EMAIL = 'nmtcanary@gmail.com'
PASSWORD = 'NewMexicoTech'
phonebook = []
voice = Voice()

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
            command = raw_input('Canary>')
            command = command.lower().split()
            if command[0] in ('quit','exit'):
                return
            if command[0] in ('ls','list'):
                print dir(commands)
                continue
            if command[0] in ('clear','cls'):
                os.system(['clear','cls'][os.name=='nt'])
                continue
            getattr(commands,command[0],commands.not_found)(voice, phonebook,command)
        except (KeyboardInterrupt, SystemExit):
            print '\n'
            print '\aProcess Cancelled'
            print
        except:
            print ('\aAn Error Occured:')
            print_exc()
            print

def main(argv):
    #load_phone_list()
    login()
    if len(argv) is 0:
        print "Miner's Canary"
        shell()
        return 0
    print 'Only shell is active currently'
    print 'To activate, run "python canary.py" with no arguments'
    return -1

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
