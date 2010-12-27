#!/usr/bin/python -tt
#  dicttest 1

from sys import argv
import os

program_name = argv[0]
u = []

def emptyFunction(f):
    pass

def file_load(filename):
    return open(filename, 'rU')

def nickColumn2list():
    for line in file_load('utfil'):
        nick = line.split()[1]
        if not nick in u: 
            u.append(nick)
    return u

def find_nick(nick, column):
    if nick in column:
        return True

def aHref(url, nick):
    print '<a href="%s" alt="%s">' % (url, nick)

def main():
    nickColumn2list()
#    for line in file_load('utfil'):
        # only true on first value in column
        #        if find_nick('tugg', line.split()[1]):
            #            aHref(line.split()[2], line.split()[1])
            #        else:
                #            print 'nej'
                #            break

if __name__ == '__main__':
    main()
