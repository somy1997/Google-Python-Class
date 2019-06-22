#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib
import urllib2

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""

def sorturl(aurl) :
  match = re.search(r'-(\w+)-(\w+)\.\w+',aurl)
  if match :
    return match.group(2)
  else :
    return aurl

def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  # +++your code here+++
  hindex = filename.index('_')
  host = 'http://' + filename[hindex + 1:]
  listurl = []
  f = open(filename,'rU')
  for line in f :
    match = re.search(r'GET (\S+) ',line)
    if 'puzzle' in match.group(1) :
      puzurl = host + match.group(1)
      if puzurl not in listurl :
        listurl.append(puzurl)
  sortedurls = sorted(listurl,key = sorturl)
  return sortedurls
  
def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  # +++your code here+++
  if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)
  f = open(os.path.join(dest_dir,'index.html'),'w')
  f.write('<html><body>\n')
  i = 0
  proxy = urllib2.ProxyHandler({'http': '10.3.100.207:8080'})
  opener = urllib2.build_opener(proxy)
  urllib2.install_opener(opener)
  for img_url in img_urls :
    imgname = 'img%d.jpg' % i
    print 'Retrieving...',img_url
    with open(os.path.join(dest_dir,imgname),'wb') as p:
      p.write(urllib2.urlopen(img_url).read())
      p.close()
    f.write('img src= "%s"' %(imgname))
    i+=1
  f.write('\n<\body><\html>\n')
  f.close()
  
  

def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: [--todir dir] logfile '
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)
  else:
    print '\n'.join(img_urls)

if __name__ == '__main__':
  main()
