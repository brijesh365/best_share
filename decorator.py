import traceback
from error import (GeneralError, ValidateError, UnhandledError)
"""
    raise exception decorator used to raise exception for a method.
"""
def raise_exception(func):
    def wrapper(self):
        try:
            return func(self)
        except (GeneralError, IOError, ValidateError):
            raise
        except:
            raise UnhandledError(traceback.format_exc())
    return wrapper
