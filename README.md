# selenium-python-automation
It is a Selenium test automation framework writtten in Python

To set up framework, do following instruction:

1. keep your xpath and/or css selector in variables/paths_and_selectors.txt file. There is an type and value list for selectors. firt item of is type of calling selector and second item is calue of selector. you can see type of selectors at the satrt of file. It is the most important of framework, if need to change selectors(for maintenance), just change that file. no need to change Python code itself.
2. create a new package for your test files. one example in project is "tetcasepack". you can copy of a template from variables/NewTemplate.py file. 
3. All Selenium related functions are keep in variables/SeleniumFunctions.py file. insead of using native functions in testcase, the are in a user friendly and loggable format.
4. To produce output, there is a html runner. variables/HTMLTestRunner.py you can setup output folder and file name name settings in  def runnerSuite that in variables/GeneralFunctions.py file.

