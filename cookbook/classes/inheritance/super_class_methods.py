"""
    super_class_methods.py
    ----------------------------  
    Showing inheriting and overriding class methods and attributes from parent class.
"""
from cookbook.classes.utils import iso6346


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
    def create_empty(cls, owner_code, *args, **kwargs):
        """class method with extra parameters"""
        return cls(owner_code, contents=None, *args, **kwargs)

    @classmethod
    def create_with_items(cls, owner_code, items, *args, **kwargs):
        """class method with extra parameters"""
        return cls(owner_code, contents=list(items), *args, **kwargs)

    def __init__(self, owner_code, contents):
        """instance attribute"""
        self.owner_code = owner_code
        self.contents = contents
        self.bic = self._make_bic_code(
            owner_code=owner_code,
            serial=ShippingContainer._get_next_serial()
        )


class RefrigeratedShippingContainer(ShippingContainer):
    """SubClass of ShippingContainer"""

    MAX_CELSIUS = 4.0

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(
            owner_code=owner_code,
            serial=str(serial).zfill(6),
            category='R'
        )

    def __init__(self, owner_code, contents, celsius):
        super().__init__(owner_code, contents)
        if celsius > RefrigeratedShippingContainer.MAX_CELSIUS:
            raise ValueError("Too Hott")
        self.celsius = celsius


__test__ = {
    'RefrigeratedShippingContainer': '''
        >>> r = RefrigeratedShippingContainer.create_with_items('ESC', ['brocolli', 'cauliflower', 'carrots'],  celsius=2.0)
        >>> r.__class__.__base__.__name__
        'ShippingContainer'
        >>> r._make_bic_code("YML", 1234)
        'YMLR0012340'
    '''
}


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
