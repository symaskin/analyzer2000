#!/usr/bin/python -tt
#  dicttest 1

from sys import argv
import os
import re
from collections import defaultdict

d = defaultdict()
program_name = argv[0]
nicks_in_file = []
urls_in_file = []
nicks_and_url = {}
i = []

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

def print_urls():
    for i in file_load('utfil'):
        #urls_in_file.append(i.split()[2])
        print i.split()

def aHref(url, nick):
    print '<a href="%s" alt="%s">' % (url, nick)

def main():
    nickColumn2list()
    #    print_urls()
    #    for line in file_load('utfil'):
#           print line.split()

if __name__ == '__main__':
    main()
