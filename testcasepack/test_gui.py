# -*- coding: UTF-8 -*-
import unittest
import logging
import time
from selenium.webdriver.common.by import By
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
 
    def mahsumnet_01_wait_pure_ajax_complete(self):
        # Testcase description: fill the form, wait for ajax progess is complete and check result text
        test_case_name      = g.get_test_case_name(self)       
        v_first_name        = g.v("SeleniumPage", "v_first_name")
        v_last_name         = g.v("SeleniumPage", "v_last_name")
        v_value_list        = g.v("SeleniumPage", "v_value_list")
        v_index_list        = g.v("SeleniumPage", "v_index_list")
        v_text_list         = g.v("SeleniumPage", "v_text_list")
        v_check_box         = g.v("SeleniumPage", "v_check_box")
        v_pure_ajax_btn     = g.v("SeleniumPage", "v_pure_ajax_btn")
        v_ajax_progress     = g.v("SeleniumPage", "v_ajax_progress")
        v_result_div        = g.v("SeleniumPage", "v_result_div")
        v_ajax_result_text  = g.v("SeleniumPage", "v_ajax_result_text")
              
        g.start_test_message(date_as_string, test_case_name)
         
        s.go_to_page("mahsumakbas_net","selenium_page")
        s.type_element(v_first_name, "Mahsum")
        s.type_element(v_last_name, "Akbas")
        s.select_element_from_list_by_value(v_value_list, "value3")
        s.select_element_from_list_by_index(v_index_list, "1")
        s.select_element_from_list_by_text(v_text_list, "text5")
        s.click_element(v_check_box, "Checkbox element")
        s.click_element(v_pure_ajax_btn, "Pure ajax button")
        s.wait_element_to_be_invisible(v_ajax_progress, "Ajax progress image")
        s.assertElementPresent(self, v_result_div, "Result object is not exist")
        s.assertElementPresent(self, v_ajax_result_text, "Result text object is not exist")
        s.assertEqualElementText(self, v_ajax_result_text, "It is a pure ajax response text")
        
        g.finish_test_message(date_as_string, test_case_name)
          
    def mahsumnet_02_default_number_of_articles(self):
        # Testcase description: check number of articles on page is deafult 10 
        test_case_name      = g.get_test_case_name(self)       
        v_articles          = g.v("HomePage", "v_articles")
                      
        g.start_test_message(date_as_string, test_case_name)
         
        s.go_to_page("mahsumakbas_net","home_page")
        number_of_articles  = str(s.get_element_length(v_articles))
        s.assertEqualValues(self, "10", number_of_articles, "Number of default article is not 10 on home page")

        g.finish_test_message(date_as_string, test_case_name)

    def mahsumnet_03_first_article_name(self):
        # Testcase description: check title of the first article on page
        test_case_name      = g.get_test_case_name(self)       
        v_first_article     = g.v("HomePage", "v_first_article")
           
        g.start_test_message(date_as_string, test_case_name)
         
        s.go_to_page("mahsumakbas_net","home_page")
        first_article_name  = s.get_element_text(v_first_article)
        s.assertEqualValues(self, "Drag and Drop Operation in Selenium", first_article_name, "The name of first article is not correct")

        g.finish_test_message(date_as_string, test_case_name)
        
    def mahsumnet_04_about_me_title(self):
        # Testcase description: check title of "about me" page
        test_case_name      = g.get_test_case_name(self)       
        v_page_title         = g.v("AboutMePage", "v_page_title")
              
        g.start_test_message(date_as_string, test_case_name)
         
        s.go_to_page("mahsumakbas_net","about_me")
        first_article_name  = s.get_element_text(v_page_title)
        s.assertEqualValues(self, "About Me", first_article_name, "The title of page is not correct")

        g.finish_test_message(date_as_string, test_case_name)   
            
    def tearDown(self): 
        s.quit_driver()
        
if __name__ == '__main__':
    GF.runnerSuite(GF(), date_as_string, TestClass)