'''
student.py
#   Created on Sun Aug 21 2011 by Arctem
'''

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
    time_restriction = []

    def __init__(self, name, number, gender, year, hall, roomnum, clubs, major, minor):
        self.name = name
        self.number = number
        self.gender = gender
        self.year = year
        self.hall = hall
        self.roomnum = roomnum
        self.clubs = clubs
        self.major = major
        self.minor = minor
        
    def set_value(self, newname = name, num = number, gend = gender, y = year, h = hall, rnum = roomnum):
        self.name = newname
        self.number = num
        self.gender = gend
        self.year = y
        self.hall = h
        self.roomnum = rnum
