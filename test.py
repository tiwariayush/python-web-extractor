from extract import extract
import unittest

class TestProductinfoExtractor(unittest.TestCase):
   
   def setUp(self):
      pass
    
   def testOne(self):
     '''
       The extract function should return a dict on execution with urls having the xpath in the website_csv list
     '''
     empty_dict = {}
     type_empty_dict = type(empty_dict)
     self.assertEqual(type(extract('http://www.flipkart.com/scullers-men-s-checkered-casual-shirt/p/itmduvc4fpgtktkf?pid=SHTDUJF6XSSNB92T&srno=b_1&ref=884be278-844c-4a29-b300-b0c131dfddb0')) , type_empty_dict)

if __name__ == '__main__':
  unittest.main()
