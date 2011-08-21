'''
canarydata.py
#   Created on Sun Aug 21 2011 11:24 GMT -0600 by Arctem
'''
import os.path

phonebookdir = '/dat/phonebook.candat'
phonebook = []

def load_phonebook():
    ensure_dir('dat')
    if not os.path.exists(phonebookdir):
        phonebook_file = open(phonebookdir, 'w')
        pickle.dump(phonebook, phonebook_file)
        phonebook_file.close()
    open(phonebookdir, 'r')
    phonebook = pickle.load(phonebook_file)
    phonebook_file.close()

    
def ensure_dir(f):
    d = os.path.dirname(f)
    if not os.path.exists(d):
        os.makedirs(d)

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