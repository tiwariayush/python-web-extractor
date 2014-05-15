from extract import extract
import unittest

class TestProductinfoExtractor(unittest.TestCase):
   
   def setUp(self):
      pass
   
   def testCheckUrl(self):
     '''
       Validates the url
     '''
     urls_for_validation = ['google.com','https://flipkart.com/ayush','https://amazon.com']
     with self.assertRaises(NameError) as context:
         for url in urls_for_validation:
           extract(url)
     self.assertEqual(context.exception.message , 'Invalid URL given')
    
   def testCheckFlipkart(self):
     '''
       The extract function should return a dict on execution with urls having the xpath in the website_csv list
     '''
     item_name = "Scullers Men's Checkered Casual Shirt"
     item_name_extracted = str(extract('http://www.flipkart.com/scullers-men-s-checkered-casual-shirt/p/itmduvc4fpgtktkf?pid=SHTDUJF6XSSNB92T&srno=b_1&ref=884be278-844c-4a29-b300-b0c131dfddb0')['name']).replace("\n","").replace(" ","")
     self.assertEqual(item_name.replace(" ","") , item_name_extracted)
  
   def testCheckAmazon(self):

     item_name = "MIDLAND WR300 Weather Radio"
     item_name_extracted = str(extract('http://www.amazon.com/Midland-WR-300-MIDLAND-WR300-Weather/dp/B00009V2YV/ref=sr_1_1?m=A21C4U5X700J66&s=aht&ie=UTF8&qid=1399984417&sr=1-1')['name']).replace('\n',"").replace(' ','')
    
     self.assertEqual(item_name.replace(" ","") , item_name_extracted)


if __name__ == '__main__':
  unittest.main()
