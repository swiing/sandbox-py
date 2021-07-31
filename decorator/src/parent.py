"""Parent class"""

import functools
import glob
import logging

logging.basicConfig(level=logging.DEBUG)


print(glob.glob('*.py'))

class Parent:
    """Parent class"""

    __logger = logging.getLogger(__name__)
    _private = 0
    __mangled = 0

    @staticmethod
    def decorated(run):
        @functools.wraps(run)
        def wrapper(self, **kwargs):
            self.__logger.info("In wrapper")
            getattr(self, "_" + type(self).__name__ + "__logger").info("In wrapper - de-mangling name")
            return run(self, **kwargs)
        return wrapper
    
    def __init__(self, **kwargs):
        #self._private = 1
        #self.__mangled = 1
        pass

    # def print(self):
        # print("private", self._private)
        # print("mangled", self.__mangled)
        # self.__logger.info("logging message")

