#!/usr/bin/env python
# encoding: utf-8
'''
canary.py
#   Created on Sun Aug 21 2011 11:01 GMT -0600 by Izzy Cecil & Fuzzo & Arctem
'''

from googlevoice import Voice, input

email = ''
password = ''
phonebook = {}
voice = Voice()

def shell():
    while True:
        try:
            command = input('Canary>')
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
    #login()
    if len(argv) is 0:
        print "Minor's Canary"
        shell()
        return 0
    print 'Only shell is active currently'
    print 'To activate, run "python canary.py" with no arguments'
    return -1

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
