

class Vector:
    """ How a class is represented as an object"""

    def __init__(self, **kwargs):
        private = {'_' + k: v for k, v in kwargs.items()}
        self.__dict__.update(private)

    def __getattr__(self, name):
        print("name=", name)

    def __repr__(self):
        return "{}({})".format(
            self.__class__.__name__,
            ', '.join("{k}={v}".format(k=k, v=self.__dict__[k])
                      for k in sorted(self.__dict__.keys())))
