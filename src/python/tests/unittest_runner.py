import unittest
import xmlrunner

test_suite = unittest.TestSuite()
for test_cases in unittest.defaultTestLoader.discover('.', pattern='test_*.py'):
    for test_case in test_cases:
        test_suite.addTests(test_case)

test_runner = xmlrunner.XMLTestRunner(output="./result")
test_runner.run(test_suite) 
