import sys
import traceback

from error import *
from general import General
from messages import ARGUMENT_MSG
from decorator import raise_exception

class BestShare(General):
    def __init__(self, *args, **kwargs):
        """
            Intializes General class with filename, so it can be used for
            reading.
        """
        super(BestShare, self).__init__(args[0])
        self.companyshares = []

    @raise_exception
    def bestshare(self):
        """
            This functions calculates month, year in which the share price 
            was highest for each company.

            NOTE: return is needed to satisfy test_share.py(unit test cases)
        """
        data = self.readfile()
        col_length = len(data[0])
        row_length = len(data)
        for colIndex in xrange(2, col_length):
            bestrowIndex = 1
            for rowIndex in xrange(2, row_length):
                if int(data[rowIndex][colIndex]) >= int(data[bestrowIndex][colIndex]):
                    bestrowIndex = rowIndex

            self.companyshares.append("%s, %s, %s, %s" % \
                                      (data[0][colIndex],
                                      data[bestrowIndex][0],
                                      data[bestrowIndex][1],
                                      data[bestrowIndex][colIndex]))
        return self.companyshares

if __name__ == "__main__":
    try:
        if len(sys.argv) != 2:
            raise ArgumentError(ARGUMENT_MSG)
        bestshare_obj = BestShare(sys.argv[1])
        companyshares = bestshare_obj.bestshare()

        #
        # NOTE Display Company shares.
        #
        for _ in companyshares:
            print _

    except(ValidateError, GeneralError, ArgumentError, IOError,
           UnhandledError) as obj:
        print "\n\t%s: %s\n" % (obj.__class__.__name__, obj)
