#!usr/bin/python
#-*- coding: utf-8 -*- 

import sys
import os
import csv
from urlparse import urlparse

try:                                                                                 #Checking for odule import exceptions
  from webscraping import download , xpath 
except ImportError: 
  print('No webscraping module found , try installing it ') 
  sys.exit()

def extract(url):
  '''
  Function that extracts product info from websites listed in the csv page . It takes the url as an argument.
  '''
  try:
      url = url.encode('utf-8')
      D = download.Download()

      try: 
       f = open(os.path.join(os.path.dirname(__file__),'webpage_xpath.csv'), 'rb')  #Joining absolute path so that the function can be used inside an app
      except IOError:                                                               # Checking for Input Output exceptions, i.e if the file exists or not
       print('An error occured while reading the csv file, check your Directory again')
       sys.exit()
   
      reader = csv.reader(f)
      row = list(reader)
      item ={}
      for r in range(0,5):
        if url.find(row[r][0])>=0:
          xpath1 = row[r][1]
          xpath2 = row[r][2]
          xpath3 = row[r][3]  

          html = D.get(url)
      
          item['name'] = xpath.get(html,'%s//text()' % xpath1)
          item['price'] = xpath.get(html,'%s//text()' % xpath2)
          item['image'] = xpath.get(html, '%s' % xpath3)
          return item
          sys.exit()

        else:
          continue
  
      if item == {}: 
        print "Invalid url given"
        sys.exit()

      sys.exit()

  except KeyboardInterrupt:                                                         #Prints Goodbye in case of keyboard interruption     
    print ('Goodbye')
    sys.exit()

if __name__ == '__main__':
   url="".join( sys.argv[1:] )
   extract(url)
   sys.exit()
