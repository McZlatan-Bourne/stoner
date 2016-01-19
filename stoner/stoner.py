#!/usr/bin/env python

import sys
import ftplib
from fileHelper import checkfile
from dirHelper import getCurrentDirectory

try:
    if sys.argv[1] == '-s' or sys.argv[1] == '--stone':
        try:
            u_file = checkfile(sys.argv[2])
            ADDRESS = raw_input('FTP Server Address: ')
            USERNAME = raw_input('FTP Server Username: ').lower()
            PASSWORD = raw_input('FTP Server Password: ')
            if u_file is not False:
                ftp = ftplib.FTP(ADDRESS, USERNAME, PASSWORD) 
                file = open(u_file, 'rb')
                import os
                os.system("clear")
                print "..................." + "\n" + "Uploading ..."
                ftp.storbinary('STOR ' + str(u_file), file)
                print "..................." + "\n" + "Upload Complete ..." + "\n" + "..................."
                file.close()
                ftp.quit()
            elif u_file is False:
                print "File not found"
        except Exception: print "Something wicked and unusual happened."
    elif sys.argv[1] == '-d' or sys.argv[1] == '--cwd':
            try:
                print getCurrentDirectory()
            except Exception: print "Error: Could not rertrieve current working directory"
    else:
            print "USAGE: stoner -s [--stone] filename.ext" + "\n" + "       stoner -d [--cwd]"
except Exception: print "USAGE: stoner -s [--stone] filename.ext" + "\n" + "       stoner -d [--cwd]"
