"""Child class"""

import logging

from parent import Parent


class Child(Parent):
    __logger = logging.getLogger(__name__)
    _private = 1
    __mangled = 1

    @Parent.decorated
    def print2(self):
        print("private", self._private)
        print("mangled", self.__mangled)
        self.__logger.info("logging message")