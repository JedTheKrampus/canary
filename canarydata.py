'''
canarydata.py
#   Created on Sun Aug 21 2011 11:24 GMT -0600 by Arctem
'''
import os.path
import pickle
from student import Student
import canary

phonebookdir = 'dat/phonebook.candat'
phonebook = []

def load_phonebook(debug):
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
    if debug:
        print phonebook
    else:
        print 'Loaded phonebook data for {} students.'.format(len(phonebook))

def save_phonebook():
    phonebook_file = open(phonebookdir, 'w')
    try:
        pickle.dump(phonebook, phonebook_file, 2)
    except:
        print 'Error saving phonebook.'
    phonebook_file.close()
    
def add_student(student):
    phonebook.append(student)
    save_phonebook()
    
def ensure_dir(f):
    d = os.path.dirname(f)
    if not os.path.exists(d):
        os.makedirs(d)
