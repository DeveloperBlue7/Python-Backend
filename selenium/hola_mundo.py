import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver


class hola_mundo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')
        driver = cls.driver
        driver.implicitly_wait(10)
    
    def test_hola_mundo(self):
        driver = self.driver
        driver.get('https://platzi.com')
        
    def test_visit_wikipedia(self):
        self.driver.get('https://www.wikipedia.org')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        
if __name__ == "__main__":
    unittest.main(verbosity= 2, testRunner= HTMLTestRunner(output= 'reportes', report_name='hola_mundo_report'))