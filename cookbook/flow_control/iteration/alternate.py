

class AlternateIterable:

    def __init__(self):
        self.data = [1, 2, 3]

    def __getitem__(self, idx):
        return self.data[idx]


__test__ = {
    'AlternateIterable':'''
    >>> from alternate import AlternateIterable
    >>> [i for i in AlternateIterable()]
    [1, 2, 3]
    '''
}


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)