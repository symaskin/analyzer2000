#!/usr/bin/python -tt
#  dicttest 1

from sys import argv
import os

program_name = argv[0]
nicks_in_file = []
nicks_and_url = {}
i = []
def emptyFunction(f):
#    for line in file_load('utfil'):
        # only true on first value in column
        #        if find_nick('tugg', line.split()[1]):
            #            aHref(line.split()[2], line.split()[1])
            #        else:
                #            print 'nej'
                #            break
    pass

def file_load(filename):
    return open(filename, 'rU')
    filename.close()

def nickColumn2list():
    for line in file_load('utfil'):
        nick = line.split()[1]
        url = line.split()[2]
        if not nick in nicks_in_file: 
            nicks_in_file.append(nick)
    return nicks_in_file

def find_nick(nick, listan):
    if nick in listan:
        return True

def aHref(url, nick):
    print '<a href="%s" alt="%s">' % (url, nick)

def main():
    
    nickColumn2list()

if __name__ == '__main__':
    main()
