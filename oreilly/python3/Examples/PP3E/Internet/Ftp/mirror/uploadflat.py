#!/bin/env python 
##############################################################################
# use ftp to upload all files from one local dir to a remote site/directory;
# e.g., run me to copy a web/ftp site's files from your PC to your ISP;
# assumes a flat directory upload: uploadall.py does nested directories.
# see downloadflat.py comments for more notes: this script is symmetric.
##############################################################################

import os, sys, ftplib
from getpass import getpass
from mimetypes import guess_type

nonpassive = False                                  # passive ftp by default
remotesite = 'home.rmi.net'                         # upload to this site
remotedir  = '.'                                    # from machine running on
remoteuser = 'lutz'
remotepass = getpass('Password for %s on %s: ' % (remoteuser, remotesite))
localdir   = (len(sys.argv) > 1 and sys.argv[1]) or '.'
cleanall   = raw_input('Clean remote directory first? ')[:1] in ['y', 'Y']

print 'connecting...'
connection = ftplib.FTP(remotesite)                 # connect to ftp site
connection.login(remoteuser, remotepass)            # login as user/password
connection.cwd(remotedir)                           # cd to directory to copy
if nonpassive:                                      # force active mode ftp
    connection.set_pasv(False)                      # most servers do passive

if cleanall:
    for remotename in connection.nlst():            # try to delete all remotes
        try:                                        # first to remove old files
            print 'deleting remote', remotename
            connection.delete(remotename)           
        except:                                     
            print 'cannot delete remote', remotename

count = 0                                           # upload all local files
localfiles = os.listdir(localdir)                   # listdir() strips dir path
                                                    # any failure ends script
for localname in localfiles:
    mimetype, encoding = guess_type(localname)      # eg ('text/plain', 'gzip')
    mimetype  = mimetype or '?/?'                   # may be (None, None)
    maintype  = mimetype.split('/')[0]              # .jpg ('image/jpeg', None')

    localpath = os.path.join(localdir, localname) 
    print 'uploading', localpath, 'to', localname,
    print 'as', maintype, encoding or ''
    if maintype == 'text' and encoding == None:
        # use ascii mode xfer
        localfile = open(localpath, 'r')
        connection.storlines('STOR ' + localname, localfile)
    else:
        # use binary mode xfer
        localfile = open(localpath, 'rb')
        connection.storbinary('STOR ' + localname, localfile)
    localfile.close()
    count += 1

connection.quit()
print 'Done:', count, 'files uploaded.' 
