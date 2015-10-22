""" RobotX Tests Trigger

This is for running all RobotX tests.

Usage: python runtests.py

"""

import os
import tempfile
import unittest
import shutil
import traceback

from robot import run

class RunTestCase(unittest.TestCase):
    def setUp(self):
        self.test_path = os.path.curdir
        tmp_path = tempfile.gettempdir()
        self.output_dir = os.path.join(tmp_path, "robotx_test_result")
        if (os.path.exists(self.output_dir)):
            shutil.rmtree(self.output_dir)
        os.mkdir(self.output_dir)
        self.output_file = os.path.join(self.output_dir, "output.xml")
        self.log_file = os.path.join(self.output_dir, "log.html")
        self.report_file = os.path.join(self.output_dir, "report.html")
        self.suites = ["test_cmd_*"]

    def test_run(self):
        try:
            run(self.test_path,
                suite=self.suites,
                outputdir=self.output_dir,
                output=self.output_file,
                log=self.log_file,
                report=self.report_file)
        except Exception as excpetion:
            self.fail("robot.run() raised a Exception.\n%s" % traceback.print_exc())

if __name__ == '__main__':
    unittest.main()
