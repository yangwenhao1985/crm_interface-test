__author__ = 'Michael'

import unittest
from common import data
import HTMLTestRunner

test_list = data.test_model()
suite = unittest.TestSuite()

if __name__ == "__main__":
    for test_file in test_list:
        suite.addTest(unittest.defaultTestLoader.loadTestsFromName(test_file))
    fp = open("E:\\crm_interface-test\\report\\result.html", "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="Interface_Test_Report", description="CRM_APP&WEB_Report")
    runner.run(suite)