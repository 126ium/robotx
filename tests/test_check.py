import unittest
import os
import traceback

from robotx.core.commands import check

class FakeOpts(dict):
    def __init__(self):
        super(FakeOpts, self).__init__()
        self.cases = ''
        self.is_tcms = ''
        self.plan_id = ''

class CheckCmdTestCase(unittest.TestCase):
    def setUp(self):
        current_path = os.path.dirname(os.path.realpath(__file__))
        cases_path = os.path.join(current_path, 'Demo')
        self.opts = FakeOpts()
        self.opts.cases = cases_path
        self.opts.is_tcms = None
        self.opts.plan_id = None

    def test_check(self):
        check_cmd = check.Command()
        try:
            check_cmd.run(args=[], opts=self.opts)
        except Exception as exception:
            self.fail('Check cases failed.\n%s' % traceback.print_exc())

if __name__ == '__main__':
    unittest.main()