'''
canarydata.py
#   Created on Sun Aug 21 2011 11:24 GMT -0600 by Arctem
'''
import os.path
import pickle

phonebookdir = 'dat/phonebook.candat'
phonebook = []

def load_phonebook():
    global phonebook
    ensure_dir('dat/')
    if not os.path.exists(phonebookdir):
        phonebook_file = open(phonebookdir, 'w')
        try:
            pickle.dump(phonebook, phonebook_file, 2)
            phonebook_file.close()
        except:
            phonebook_file.close()
            os.remove(phonebookdir)
            print 'fatal: Phonebook file could not be found or created.'
            exit()
    phonebook_file = open(phonebookdir, 'r')
    phonebook = pickle.load(phonebook_file)
    phonebook_file.close()
    print phonebook

    
def ensure_dir(f):
    d = os.path.dirname(f)
    if not os.path.exists(d):
        os.makedirs(d)

load_phonebook()

class Student:
    name = ''
    number = ''
    gender = None
    year = None
    hall = None
    roomnum = 0
    clubs = []
    major = []
    minor = []