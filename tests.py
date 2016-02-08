try: import unittest2 as unittest #for Python <= 2.6
except: import unittest
import os
import sys
sys.path.append(os.getcwd() + '/modules')

from selenium import webdriver


#default URL routing
tweetsec_eval_url =  'http://127.0.0.1:8000/tweetsec/default/evaluator' 



class FunctionalTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(2)


    @classmethod    
    def tearDownClass(self):
        self.browser.close()


        
def run_functional_tests(pattern=None):
    print 'running tests'
    if pattern is None:
        tests = unittest.defaultTestLoader.discover('fts')
    else:
        pattern_with_globs = '*%s*' % (pattern,)
        tests = unittest.defaultTestLoader.discover('fts', pattern=pattern_with_globs)

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(tests)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        
        run_functional_tests()
    else:
        
        run_functional_tests(pattern=sys.argv[1])
