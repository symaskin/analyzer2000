#!/usr/bin/python -tt
#  dicttest 1

from sys import argv
import os

program_name = argv[0]

def emptyFunction(f):
    pass

def file_load(filename):
    return open(filename, 'rU')

def aHref(url, nick):
    print '<a href="%s" alt="%s">' % (url, nick)

def main():
    for line in file_load('testfil'):
        aHref(line.split()[2], line.split()[1])

if __name__ == '__main__':
    main()
