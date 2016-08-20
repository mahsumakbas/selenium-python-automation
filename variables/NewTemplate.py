# -*- coding: UTF-8 -*-
import unittest
import logging
from variables.GeneralFunctions import GeneralFunctions as GF
from variables.SeleniumFunctions import SeleniumFunctions as SF

g = GF()
s = SF() 

#logging.basicConfig(format='%(asctime)s : %(levelname)s: %(message)s ', level=logging.INFO, filename='C:\SeleniumLog\Logs.log')
logging.basicConfig(format='%(asctime)s : %(levelname)s: %(message)s ', level=logging.INFO)
date_as_string = g.get_date_as_string()

class TestClass(unittest.TestCase):
    def setUp(self):
        s.setup_function()
          
    def netm_ListUsers(self):
        test_case_name = g.get_test_case_name(self)       
        v_username  = g.v("Login", "v_username")
              
        g.start_test_message(date_as_string, test_case_name)
         
        s.go_to_page("netmetriks","anaSayfa")
        s.type_element(v_username, "user1")

         
        g.finish_test_message(date_as_string, test_case_name)  
           
    def tearDown(self): 
        s.quit_driver()

if __name__ == '__main__':
    GF.runnerSuite(GF(), date_as_string, TestClass)