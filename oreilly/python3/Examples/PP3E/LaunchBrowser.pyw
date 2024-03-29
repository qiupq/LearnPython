#!/bin/env python
#############################################################################
# Launch a web browser to view a web page, portably.  If run in '-live' 
# mode, assumes you have a Internet feed and opens page at a remote site.
# Otherwise, assumes the page is a full file path name on your machine, 
# and opens the page file locally.  On Unix/Linux, finds first browser 
# on your $PATH.  On Windows, tries DOS "start" command first, or searches
# for the location of a browser on your machine for os.spawnv by checking
# PATH and common Windows executable directories. You may need to tweak 
# browser executable name/dirs if this fails. This has only been tested in
# Windows and Linux; you may need to add more code for other machines (mac:
# ic.launcurl(url)?). See also the new standard library webbrowser module.
#############################################################################

import os, sys
from Launcher import which, guessLocation     # file search utilities
useWinStart = True                            # 0=ignore name associations
onWindows   = sys.platform[:3] == 'win'

def launchUnixBrowser(url, verbose=True):         # add your platform if unique
    tries = ['netscape', 'mosaic', 'lynx']        # order your preferences here
    tries = ['firefox'] + tries                   # firefox rules!
    for program in tries:
        if which(program): break                  # find one that is on $path
    else:
        assert 0, 'Sorry - no browser found'
    if verbose: print 'Running', program
    os.system('%s %s &' % (program, url))         # or fork+exec; assumes $path

def launchWindowsBrowser(url, verbose=True):
    if useWinStart and len(url) <= 400:           # on windows: start or spawnv
        try:                                      # spawnv works if cmd too long
            if verbose: print 'Starting'       
            os.system('start ' + url)             # try name associations first
            return                                # fails if cmdline too long
        except: pass
    browser = None                                # search for a browser exe
    tries   = ['IEXPLORE.EXE', 'netscape.exe']    # try explorer, then netscape
    tries   = tries + ['firefox.exe']
    for program in tries:
        browser = which(program) or guessLocation(program, 1)
        if browser: break
    assert browser != None, 'Sorry - no browser found'
    if verbose: print 'Spawning', browser
    os.spawnv(os.P_DETACH, browser, (program, url))

def launchBrowser(Mode='-file', Page='index.html', Site=None, verbose=True):
    if Mode == '-live':
        url = 'http://%s/%s' % (Site, Page)       # open page at remote site
    else:
        url = 'file://%s' % Page                  # open page on this machine
    if verbose: print 'Opening', url
    if onWindows:
        launchWindowsBrowser(url, verbose)        # use windows start, spawnv
    else:
        launchUnixBrowser(url, verbose)           # assume $path on unix, linux

if __name__ == '__main__':
    # defaults
    Mode = '-file'
    Page = os.getcwd() + '/Internet/Web/PyInternetDemos.html'
    Site = 'starship.python.net/~lutz'

    # get command-line args
    helptext = "Usage: LaunchBrowser.py [ -file path | -live path site ]"
    argc = len(sys.argv)
    if argc > 1:  Mode = sys.argv[1]
    if argc > 2:  Page = sys.argv[2]
    if argc > 3:  Site = sys.argv[3]
    if Mode not in ['-live', '-file']:
        print helptext
        sys.exit(1)
    else:
        launchBrowser(Mode, Page, Site)
