

class ShippingContainer:
    """class attribute"""
    next_serial = 1337

    @staticmethod
    def _get_next_serial():
        result = ShippingContainer.next_serial
        ShippingContainer.next_serial += 1
        return result

    def __init__(self, owner_code, contents):
        """instance attribute"""
        self.owner_code = owner_code
        self.contents = contents
        self.serial = ShippingContainer._get_next_serial()


__test__ = {
    'ShippingContainer': '''
        >>> ShippingContainer(5, 'car')._get_next_serial()
        1338
        >>> ShippingContainer(56, 'car').serial
        1339
    '''
}


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
