import traceback
from error import ValidateError
from messages import HEADER_MSG, VALIDATION_MSG
from decorator import raise_exception

class General(object):
    """
        General class read data from file and validates it.
    """
    def __init__(self, filename):
        self.filename = filename

    @raise_exception
    def readfile(self):
        """
            Read and validates file.
        """
        data = [ row.strip().split(",") for row in open(self.filename) if row != '' ]
        self.validatefile(data)
        return data

    def validatefile(self, data):
        #
        # NOTE: Can put more validaton here.
        #
        header_length = len(data[0])
        if data[0][0].capitalize() != "Year":
            raise ValidateError(VALIDATION_MSG % self.filename)

        for row in data[1:]:
            if header_length != len(row):
                raise ValidateError(HEADER_MSG % (", ".join(row), self.filename))
