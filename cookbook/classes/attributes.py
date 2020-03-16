

class ShippingContainer:
    """class attribute"""
    next_serial = 1337

    def __init__(self, owner_code, contents):
        """instance attribute"""
        self.owner_code = owner_code
        self.contents = contents
        self.serial = ShippingContainer.next_serial
        ShippingContainer.next_serial += 1


class ShippingContainerTwo:
    """class attribute"""
    next_serial = 1337

    def __init__(self, owner_code, contents):
        """instance attribute"""
        self.owner_code = owner_code
        self.contents = contents
        self.serial = self.next_serial
        self.serial += 1


__test__ = {
    'ShippingContainer': '''
        >>> ShippingContainer(33, "something").serial
        1337
        >>> ShippingContainer(33, "something").serial
        1338
    ''',
    'ShippingContainerTwo': '''
        >>> ShippingContainerTwo(34, "something").serial
        1338
    '''
}

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
