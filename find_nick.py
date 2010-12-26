#!/usr/bin/python -tt
# open logfile, find nick and print urls.
# test test

import re
import sys
import os
from collections import defaultdict

logfile = 'utfil'
resultDict = { 'tugg': '' }
urllist = [ ]

def add2dict(**stuff):
    print stuff


def searchLogfile(nick):
    counter = 0
    file = open(logfile, 'rU')
    for line in file:
        # nickColumn = nick kolumn
        nickColumn = line.split()[1]
        """ check if nick is present in second column of logfile. """
        if nick in nickColumn:
            url = line.split()[2]
            urllist.append(url)
            #            add2dict(nick=url)
            counter += 1
    file.close()
#    print len(resultDict.values())
    print counter, 'urls found containing', nick
    return urllist

def main():
        if len(sys.argv) >= 2:
                nick = sys.argv[1].lower()
                #searchLogfile(nick)
                print '-' * 10
                for prutt in searchLogfile(nick):
                    print prutt
        else:
                print 'usage: ', sys.argv[0], '<nick>'
                sys.exit(1)

if __name__ == '__main__':
    main()
