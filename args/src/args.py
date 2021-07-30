"""A module for testing arguments"""

class AClass:
    """Just a class for testing purposes."""
    def __init__(self, *args, **kwargs):
        self.args = args
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __repr__(self):
        return str({k: getattr(self,k) 
                    for k in dir(self) if k[0:2]!="__"})

