"""
Simple example of a data class
"""
# pylint: disable=unused-import
from dataclasses import dataclass, field
import typing

@dataclass
class Customer:
    id: int
    name: str
    address: str



__test__ = {
    'Customer': '''
        >>> customer = Customer(1, "first customer", "123 Dirt Road")
        >>> customer.id
        1
        >>> customer.id = 2
        >>> repr(customer)
        "Customer(id=2, name='first customer', address='123 Dirt Road')"
        >>> customer2 = Customer(1, "first customer", "123 Dirt Road")
        >>> customer == customer2
        False
        >>> customer2.id = 2
        >>> customer == customer2
        True

    '''
}


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)