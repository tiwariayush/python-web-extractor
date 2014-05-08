import sys
import os
import csv
from urlparse import urlparse
from webscraping import download , xpath

def extract(url):
  '''
  Function that extracts product info from websites listed in the csv page . It takes the url as an argument.
  '''
  D = download.Download()

  f = open(os.path.join(os.path.dirname(__file__),'webpage_xpath.csv'), 'rb')  #Joining absolute path so that the function can be used inside an app
  reader = csv.reader(f)
  row = list(reader)
  item ={}
  for r in range(0,3):
    if url.find(row[r][0])>=0:
      xpath1 = row[r][1]
      xpath2 = row[r][2]
      xpath3 = row[r][3]  

      html = D.get(url)
      
      item['name'] = xpath.get(html,'%s//text()' % xpath1)
      item['price'] = xpath.get(html,'%s//text()' % xpath2)
      item['image'] = xpath.get(html, '%s' % xpath3)

      return item

    else:
      continue
  if item == {}: 
    item={'name':'invalid url'}
    return item

if __name__ == '__main__':
   url="".join( sys.argv[1:] )
   extract(url)
