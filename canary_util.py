#!/usr/bin/env python
# encoding: utf-8
'''
canary.py
#   Created on Sun Aug 21 2011 11:01 GMT -0600 by Izzy Cecil & Fuzzo & Arctem
'''

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
    filter_type = raw_input('What type of filter? : ')
    filter_type = filter_type.lower()
    if filter_type in ('hall'):
        halls = raw_input('Which halls?')
        halls = halls.lower().split()
        for hall in halls:
            if hall not in ('west','presidents','south','baca','driscoll'):
                print 'Hall "%s" not found...' % (hall)
                print 'Filter not added...'
                return
        filters.append((filter_type,halls))
        return
    if filter_type in ('gender'):
        gender = raw_input('Male of Female? [m/F]: ')
        if gender.lower() not in ('m','f'):
            print 'Error...'
            print 'Type "m" for Male, or "f" for Female'
            return
        filters.append((filter_type,gender))
        return
    if filter_type in ('year'):
        years = raw_input('Which years? (only undergrad, number separated by a space): ')
        years = years.split()
        for year in years:
            if year not in ('1','2','3','4','5','6'):
                print 'Error...'
                print '%s is not a valid number...' %(year)
                return
        filters.append((filter_type,years))
        return
    if filter_type in ('help','ls','list'):
        print 'Type either "hall", "gender", or "year" to create a filter of the appropriate type.'
        print 'Each will provide their own instructions for creating a filter.'
        return
