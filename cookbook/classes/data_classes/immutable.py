""" Immutable dataclass """
# pylint: disable=unused-import
from dataclasses import dataclass
import typing

@dataclass
class Customer:
    id: int
    name: str
    address: str

@dataclass(frozen=True)
class CustomerOrder(object):
    id: int
    value: float
    product: str



__test__ = {
    'CustomerOrder': '''
        >>> order = CustomerOrder(1, 10., "cheese")
        >>> order.id = 5
        Traceback (most recent call last):
            File "<stdin>", line 1, in <module>
            File "<string>", line 3, in __setattr__
        dataclasses.FrozenInstanceError: cannot assign to field 'id'
        >>> status_dict = { order: 'processed' }
        >>> status_dict
        {CustomerOrder(id=1, value=10.0, product='cheese'): 'processed'}
    '''
}


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
