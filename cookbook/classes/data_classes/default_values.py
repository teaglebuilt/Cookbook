""" Immutable dataclass """
# pylint: disable=unused-import
from dataclasses import dataclass, field
import typing
import uuid


@dataclass
class Customer:
    id: int
    name: str
    address: str


@dataclass(frozen=True, order=True)
class CustomerOrder(object):
    """ id defaults to uuid if no id is set """
    id: uuid.UUID = field(compare=False, default_factory=uuid.uuid4, init=False)
    value: float = field(compare=True)
    product: str = field(compare=False)



__test__ = {
    'CustomerOrder': '''
        >>> from default_values import *
        >>> c = CustomerOrder(10., "books")
        >>> type(c.id) == uuid.UUID
        True
    '''
}


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
