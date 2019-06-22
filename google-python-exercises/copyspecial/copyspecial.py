#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them

def extractvalids(args) :
  validpaths = []
  for adir in args :
      paths = os.listdir(adir)
      for apath in paths:
        if re.search(r'.*__\w+__.*',apath) :
          apath = os.path.join(adir,apath)
          apath = os.path.abspath(apath)
          validpaths.append(apath)
  return validpaths

def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)
    
  vps = extractvalids(args)
  
  if todir:
    if not os.path.exists(todir) :
      os.mkdir(todir)
    for apath in vps :
      filename = os.path.basename(apath) # didn't make any difference
      shutil.copy(apath,os.path.join(todir,filename))
  elif tozip:
    print 'doesn\'t work in windows'
  else :
    print '\n'.join(vps)
          
  
  # +++your code here+++
  # Call your functions
  
  
if __name__ == "__main__":
  main()
