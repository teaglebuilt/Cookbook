""" create a class that emulates defaultdict behaviour """
import collections


class MyDefaultDict(collections.UserDict):
    """ subclass UserDict """
    # pylint: disable=keyword-arg-before-vararg

    def __init__(self, default_factory=None, *args, **kwargs):
        """default_factory holds the callable used generate the default values"""
        super().__init__(*args, **kwargs)
        if not callable(default_factory) and default_factory is not None:
            raise TypeError('first argument must be callable or None')
        self.default_factory = default_factory

    def __missing__(self, key):
        if self.default_factory is None:
            raise KeyError(key)
        if key not in self:
            self[key] = self.default_factory()
        return self[key]


__test__ = {
    'MyDefaultDict': """
    """
}
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
