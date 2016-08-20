# -*- coding: UTF-8 -*-
from selenium.webdriver.common.by import *
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
import time
#from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
import os


#from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from variables.GeneralFunctions import GeneralFunctions as GF
gf = GF()

class SeleniumFunctions:    
    webdriverWaitDuration       = 30
    pageLoadTimeOut             = 30
    implicitlyWait              = 5
    

    def set_driver(self):
        global driver
        driver = webdriver.Firefox()
        #chrome_opt = webdriver.ChromeOptions()
        #chrome_opt.add_argument("--lang=tr")
        #chrome_opt.add_argument("--disable-extensions");
        #driver = webdriver.Chrome('C:\Mahsum\Test\chromedriver\chromedriver.exe', chrome_options=chrome_opt)
        #driver = webdriver.Remote("http://192.168.34.47:4444/wd/hub", chrome_opt.to_capabilities()) 
                
    def get_driver(self):
        return driver

    def quit_driver(self):
        self.get_driver().quit()
      
    def wait(self):
        return WebDriverWait(driver, self.webdriverWaitDuration)    
       
    def setup_function(self):
        self.set_driver()
        driver = self.get_driver()
        driver.implicitly_wait(self.implicitlyWait)
        driver.set_page_load_timeout(self.pageLoadTimeOut)
        driver.maximize_window()
        driver.delete_all_cookies()
       
    def go_to_page(self,baseurl,page):
        baseUrl = gf.v("HomeAddress", baseurl)
        page_tmp = gf.v("Pages", page)
        page_to_go = baseUrl+page_tmp
        driver.get(page_to_go)
        gf.consoleLog("Open page: %s" % page_to_go)

    def get_element(self, element):
        driver = self.get_driver()
        element = eval(element)
        by = "By."+element[0]
        by = eval(by)
        return  driver.find_element(by, element[1])

    
    def is_element_present(self, element):
        try:
            self.get_element(element)       
            return True
        except NoSuchElementException:
            return False

    def click_element(self, element, elementDescription):
        try:
            self.get_element(element).click()  
            gf.consoleLog(elementDescription + " is clicked")
        except NoSuchElementException:
            gf.consoleLog(elementDescription + " is not exist")
        
    def click_element_if_exist(self, element, elementDescription):
        self.get_element(element).click()  
        gf.consoleLog(elementDescription + " is clicked")

    def clear_element(self, element, elementDescription):
        self.get_element(element).clear()
        gf.consoleLog(elementDescription + " is cleared.") 
        
    def type_element(self, element, keyValue):
        self.get_element(element).send_keys(keyValue)  
        gf.consoleLog("%s is type to element." % keyValue)             
 
    def get_element_attribute(self, element, attribute):
        attr_value = self.get_element(element).get_attribute(attribute)
        return str(attr_value)
    
    def get_element_text(self, element):
        elementText = self.get_element(element).text       
        return elementText     
    
    def wait_element_to_be_visible(self, element, elementDescription):
        element = eval(element)
        by = "By."+element[0]
        by = eval(by)
        self.wait().until(EC.visibility_of_element_located((by, element[1])))
        gf.consoleLog(elementDescription + " is become visible")

    def wait_element_to_be_invisible(self, element, elementDescription):
        element = eval(element)
        by = "By."+element[0]
        by = eval(by)
        self.wait().until(EC.invisibility_of_element_located((by, element[1])))
        time.sleep(1)    
        gf.consoleLog(elementDescription+" is become invisible")
        
    def wait_element_not_to_be_presence(self, element, elementDescription):
        element = eval(element)
        by = "By."+element[0]
        by = eval(by)
        gf.consoleLog("element 1: " + element[1])
        self.wait().until_not(EC.presence_of_element_located((by, element[1])))
        time.sleep(1)    
        gf.consoleLog(elementDescription+" is become not presence")

    def wait_text_to_be_present_in_element(self, element, value):
        element = eval(element)
        by = "By."+element[0]
        by = eval(by)
        self.wait().until(EC.text_to_be_present_in_element((by, element[1]), value))
        time.sleep(1)    
        gf.consoleLog(value+" is become visible")    
        
    def switch_frame(self, frameAdi):
        driver = self.get_driver()
        driver.switch_to_frame(frameAdi)

    def exit_frame(self):
        driver = self.get_driver()
        driver.switch_to_default_content()
   
    # Assert Functions
    def assertEqualElementText(self, instance, actualElement, expectedText):
        test_case_name = gf.get_test_case_name(instance)
        screenshot_name=test_case_name+".png"
        screenshot_name=os.path.join('TestResult',screenshot_name)
        gf.consoleLog("assertEqualElementText fonksyionuna geldi")
        actualText=self.get_element_text(actualElement)
        try:    
            instance.assertEqual(expectedText,actualText,"Expected and actual text not match. Expected is: "+ expectedText + " /nActual Text is: " + actualText)
        except AssertionError:
            self.get_driver().get_screenshot_as_file(screenshot_name) 
            raise
         
    def assertNotEqualElementText(self, instance, actualElement, expectedText):
        test_case_name = gf.get_test_case_name(instance)
        screenshot_name=test_case_name+".png"
        actualText=self.get_element_text(actualElement)     
        try:    
            instance.assertNotEqual(expectedText,actualText,"Expected Text is equal to actual")
        except AssertionError:
            self.get_driver().get_screenshot_as_file(screenshot_name) 
            raise
    
    def assertEqualValues(self,instance, expectedText, actualText, errorMessage):
        test_case_name = gf.get_test_case_name(instance)
        screenshot_name=test_case_name+".png"        
        errorMessage = errorMessage  + "\nExpected value is: " + expectedText + " *** Actual value is: " + actualText
        try:    
            instance.assertEqual(actualText, expectedText, errorMessage)
        except AssertionError:
            self.get_driver().get_screenshot_as_file(screenshot_name) 
            raise
        
    def assertNotEqualValues(self,instance, expectedText, actualText, errorMessage):
        test_case_name = gf.get_test_case_name(instance)
        screenshot_name=test_case_name+".png"  
        try:    
            instance.assertNotEqual(actualText, expectedText, errorMessage)
        except AssertionError:
            self.get_driver().get_screenshot_as_file(screenshot_name) 
            raise
        
    def assertElementPartialText(self,instance, actualElement, expectedText):
        test_case_name = gf.get_test_case_name(instance)
        screenshot_name=test_case_name+".png"  
        actualText=self.get_element_text(actualElement)
        gf.consoleLog("Actual Text is: " + actualText)
        try:    
            instance.assertIn(actualText, expectedText, "Expected Text is not correct")
        except AssertionError:
            self.get_driver().get_screenshot_as_file(screenshot_name) 
            raise 

    def assertElementPresent(self,instance,element, errorMessage):
        test_case_name = gf.get_test_case_name(instance)
        screenshot_name=test_case_name+".png"  
        boolVar = self.is_element_present(element)
        gf.consoleLog("Is Element Present: " + str(boolVar))
        try:    
            instance.assertTrue(boolVar, errorMessage)
        except AssertionError:
            self.get_driver().get_screenshot_as_file(screenshot_name) 
            raise 

    def assertElementNotPresent(self,instance,element, errorMessage):
        test_case_name = gf.get_test_case_name(instance)
        screenshot_name=test_case_name+".png"  
        boolVar = self.is_element_present(element)
        gf.consoleLog("Is Element Not Present: " + str(boolVar))
        try:    
            instance.assertFalse(boolVar, errorMessage)
        except AssertionError:
            self.get_driver().get_screenshot_as_file(screenshot_name) 
            raise 

    def wait_element_not_present(self, instance,element, msg):
        test_case_name = gf.get_test_case_name(instance)
        screenshot_name=test_case_name+".png"  
        gf.consoleLog("wait_element_not_present fonskiyona geldi")
        driver = self.get_driver()
        element = eval(element)
        by = "By."+element[0]
        by = eval(by)   
        wait_time=0
        x = True
        while(x):
            try:
                driver.find_element(by, element[1])       
                x =  True
            except NoSuchElementException:
                x =  False
            if(wait_time < 120):
                time.sleep(2)
                wait_time = wait_time +2
            else:            
                try:    
                    instance.assertTrue(False, msg)
                except AssertionError:
                    self.get_driver().get_screenshot_as_file(screenshot_name) 
                    raise 
        gf.consoleLog("wait_element_not_present fonksiyonu bitti")

                    
    # Selection from Listbox functions
    def select_element_from_list_by_value(self,element,value):
        Select(self.get_element(element)).select_by_value(value)       
        gf.consoleLog(value + "  is selected from listbox")

    def select_element_from_list_by_text(self,element,value):
        Select(self.get_element(element)).select_by_visible_text(value) 
        gf.consoleLog(value + "  is selected from listbox")       
        
    def select_element_from_list_by_index(self,element,value):
        Select(self.get_element(element)).select_by_index(value) 
        gf.consoleLog(str(value) + "  is selected from listbox")           
        
    #Element functions
    def get_element_length(self, element):
        driver = self.get_driver()
        element = eval(element)
        by = "By."+element[0]
        by = eval(by)
        elementList = driver.find_elements(by, element[1])
        numOfElements = len(elementList)
        return numOfElements


    