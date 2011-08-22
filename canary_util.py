#!/usr/bin/env python
# encoding: utf-8
'''
canary.py
#   Created on Sun Aug 21 2011 11:01 GMT -0600 by Izzy Cecil & Fuzzo & Arctem
'''
class Textcolors:
    PURPLE = '\033[95m'
    OKBLUE = '\033[94m'
    PROMPT = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.END = ''

def show_text(text, filters):
    print text
    if len(filters) == 0:
        print 'To be sent to all students'
    else:
        print 'To be sent to...'
        for filt in filters:
            if filt[0] == 'hall':
                print 'Students of:'
                for hall in filt[1]:
                    print '\t%s Hall'%(hall)
            elif filt[0] == 'gender':
                print 'Students who are:'
                if filt[1] is 'm':
                    print '\tMale'
                else:
                    print '\tFemale'
            elif filt[0] == 'year':
                print 'Students in year:'
                for year in filt[1]:
                    print '\t%s'%(year)
            else:
                print filt
                print filt[0]
                print filt[0] is 'hall'
                    
def add_filter(filters):
    filter_type = raw_input(Textcolors.OKBLUE+'What type of filter? : '+Textcolors.END)
    filter_type = filter_type.lower()
    if filter_type in ('hall'):
        halls = raw_input(Textcolors.OKBLUE+'Which halls?'+Textcolors.END)
        halls = halls.lower().split()
        for hall in halls:
            if hall not in ('west','presidents','south','baca','driscoll'):
                print Textcolors.FAIL+'Hall "%s" not found...'% (hall)+Textcolors.END 
                print Textcolors.FAIL+'Filter not added...'+Textcolors.END
                return
        filters.append((filter_type,halls))
        return
    if filter_type in ('gender'):
        gender = raw_input(Textcolors.OKBLUE+'Male of Female? [m/F]: '+Textcolors.END)
        if gender.lower() not in ('m','f'):
            print Textcolors.FAIL+'Error...'+Textcolors.END
            print Textcolors.FAIL+'Type "m" for Male, or "f" for Female'+Textcoor.END
            return
        filters.append((filter_type,gender))
        return
    if filter_type in ('year'):
        years = raw_input(Textcolors.OKBLUE+'Which years? (only undergrad, number separated by a space): '+Textcolors.END)
        years = years.split()
        for year in years:
            if year not in ('1','2','3','4','5','6'):
                print Textcolors.FAIL+'Error...'+Textcolors.END
                print Textcolors.FAIL+'%s is not a valid number...'%(year) +Textcolors.END
                return
        filters.append((filter_type,years))
        return
    else:
        print 'Type either "hall", "gender", or "year" to create a filter of the appropriate type.'
        print 'Each will provide their own instructions for creating a filter.'
        return
