import unittest
import os
import tempfile
import shutil

from robotx.core.generator import generate_res
from robotx.core.generator import generate_docs
from robotx.core.generator import generate_suite
from robotx.core.generator import generate_project

class GenerateTestCase(unittest.TestCase):
    def setUp(self):
        self.current_dir = os.getcwd()
        os.chdir(tempfile.gettempdir())
        project_dir = os.path.join(os.getcwd(), 'Test_project')
        if (os.path.exists(project_dir)):
            shutil.rmtree(project_dir)
        if (os.path.exists('Test_resourse.txt')):
            os.remove('Test_resourse.txt')
        if (os.path.exists('Test_suite.txt')):
            os.remove('Test_suite.txt')

    def test_gen_project(self):
        if (os.path.exists('Test_project')):
            shutil.rmtree('Test_project')
        try:
            generate_project('Test_project')
        except Exception as excpetion:
            self.fail("generate_project() raised a Exception.\n%s" % traceback.print_exc())

    def test_gen_res(self):
        try:
            generate_res('Test_resourse.txt')
        except Exception as excpetion:
            self.fail("generate_res() raised a Exception.\n%s" % traceback.print_exc())

    def test_gen_suite(self):
        try:
            generate_suite('Test_suite.txt')
        except Exception as excpetion:
            self.fail("generate_suite() raised a Exception.\n%s" % traceback.print_exc())

    def test_gen_zdocs(self):
        if (not os.path.exists('Test_project')):
            generate_project('Test_project')
        try:
            generate_docs('Test_project')
        except Exception as excpetion:
            self.fail("generate_docs() raised a Exception.\n%s" % traceback.print_exc())

    def tearDown(self):
        os.chdir(self.current_dir)

if __name__ == '__main__':
    unittest.main()