# -*- coding: UTF-8 -*-
from variables.HTMLTestRunner import HTMLTestRunner, unittest
import time
import os
import logging
import random
import ConfigParser

class GeneralFunctions:
        
    def get_test_case_name(self,instance):
        return instance.id().split('.')[-1][10:] # Test Case Name 
    
    # get option from variable file
    def v(self, section, parameter):
        varParser = ConfigParser.RawConfigParser()
        varParserFile = os.path.join(os.path.dirname(os.path.realpath(__file__)),'paths_and_selectors.txt') 
        varParser.read(varParserFile)
        return varParser.get(section, parameter)
       
    def runnerSuite(self, date_as_string, TestClassName):
        format_report_name=date_as_string+"_TestReport.htm"
        result_file_name=os.path.join('TestResult',format_report_name)
        fp = file(result_file_name, 'ab')      
        testnames = unittest.getTestCaseNames(TestClassName,'mahsumnet_')
        suite = unittest.TestSuite()
        suite.addTests([TestClassName(methodName) for methodName in testnames])
        HTMLTestRunner(stream=fp).run(suite)
                       
    def get_date_as_string(self):
        return str(time.strftime("%Y%m%d%H%M%S"))
                    
    def start_test_message(self, LogId, testName):
        self.consoleLog("*********** Log id: " + LogId + " Test case name: "+ testName + " is started *********** ")
    
    def finish_test_message(self, LogId, testName):
        self.consoleLog("Log id: " + LogId + " Test case name: "+ testName + " is completed")
       
    def write_to_file(self,fileName, line):
        f = open(fileName, 'a')
        #f = open('C:\\SeleniumLog\\result.txt', 'a')
        f.write(line+"\n")
        f.close()
         
    def consoleLog(self, message):
        logging.info(message)
    
    def passLog(self, message):
        logging.info(message)
        
    def warningLog(self, message):
        logging.warn(message)
        
    def failLog(self, message):
        logging.error(message)
      
    def generate_random_number(self, first, last):
        randNum = random.randint(first, last)
        return randNum
            
    def directoriesFunction(self):
        self.consoleLog("dir is " + os.path.dirname(os.path.realpath(__file__)))
        self.consoleLog("getcwd is : " + os.getcwd())
        
    def sleep_system(self, second):
        time.sleep(second)
        
    
    