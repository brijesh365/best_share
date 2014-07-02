import unittest
from share import BestShare
from error import ValidateError, ArgumentError

class BestShare_Sample1(unittest.TestCase):

    def setUp(self):
        self.sample = "testcases/data-valid.csv"

    def test_correct_output(self):
        br = BestShare(self.sample)
        companyshares = br.bestshare()
        self.assertEqual(companyshares, ['Company_0, 2012, Jul, 50',
                                         'Company_1, 2013, Jan, 100',
                                         'Company_2, 2000, Dec, 150',
                                         'Company_3, 2010, Oct, 200',
                                         'Company_4, 2010, Nov, 250',
                                         'Company_5, 2013, Oct, 300',
                                         'Company_6, 2012, Jul, 350',
                                         'Company_7, 2012, Dec, 400',
                                         'Company_8, 2008, Apr, 450',
                                         'Company_9, 2007, Feb, 500'])

    def test_IO_error(self):
        br = BestShare("testcases/wrong_filename.csv")
        try:
            companyshares = br.bestshare()
        except IOError, obj:
            self.assertEqual('IOError', obj.__class__.__name__)

    def test_wrong_argument_error(self):
        br = BestShare(self.sample, 'others')
        try:
            companyshares = br.bestshare()
        except ArgumentError:
            self.assertEqual('ArgumentError', obj.__class__.__name__)

    def test_correct_argument_error(self):
        br = BestShare(self.sample)
        try:
            companyshares = br.bestshare()
        except ArgumentError:
            self.assertEqual('ArgumentError', obj.__class__.__name__)

    def test_validation_error(self):
        br = BestShare(self.sample, 'testcases/data-invalid.csv')
        try:
            companyshares = br.bestshare()
        except ValidateError:
            self.assertEqual('ValidateError,', obj.__class__.__name__)

    def test_header_mismatch_error(self):
        br = BestShare(self.sample, 'testcases/data-header-mismatch.csv')
        try:
            companyshares = br.bestshare()
        except ValidateError:
            self.assertEqual('ValidateError,', obj.__class__.__name__)

    def tearDown(self):
        pass

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(BestShare_Sample1))
    unittest.TextTestRunner(verbosity=2).run(suite)
    allsuites = unittest.TestSuite([suite])
