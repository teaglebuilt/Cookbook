"""
    super_class_methods.py
    ----------------------------
    Showing inheriting and overriding static methods.
"""
from cookbook.classes.utils import iso6346

# pylint: disable=missing-function-docstring


class ShippingContainer:
    """class attribute"""
    next_serial = 1337

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(owner_code=owner_code, serial=str(serial).zfill(6))

    @classmethod
    def _get_next_serial(cls):
        result = cls.next_serial
        cls.next_serial += 1
        return result

    @classmethod
    def create_empty(cls, owner_code):
        return cls(owner_code, contents=None)

    @classmethod
    def create_with_items(cls, owner_code, items):
        return cls(owner_code, contents=list(items))

    def __init__(self, owner_code, contents):
        """instance attribute"""
        self.owner_code = owner_code
        self.contents = contents
        self.bic = self._make_bic_code(
            owner_code=owner_code,
            serial=ShippingContainer._get_next_serial()
        )


class RefrigeratedShippingContainerTwo(ShippingContainer):
    """subclass of ShippingContainer"""

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(
            owner_code=owner_code,
            serial=str(serial).zfill(6),
            category='R'
        )


__test__ = {
    'RefrigeratedShippingContainerTwo': '''   
        >>> r = RefrigeratedShippingContainerTwo.create_with_items('ESC', ['brocolli', 'cauliflower', 'carrots'])
        >>> r._make_bic_code("YML", 1234)
        'YMLR0012340'
    '''
}

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
