'''
canarydata.py
#   Created on Sun Aug 21 2011 11:24 GMT -0600 by Arctem
'''
import os.path

phonebook = []

def load_phonebook():
    if os.path.exists('phonebook.candat'):
        phonebook = pickle.load(open('phonebook.candat'))
    

class Student:
    name
    number
    gender
    year
    hall 
    roomnum
    clubs = []
    major = []
    minor = []