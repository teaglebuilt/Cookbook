""" sortable dataclasses """
# pylint: disable=unused-import
from dataclasses import dataclass, field
import typing

@dataclass
class Customer:
    id: int
    name: str
    address: str

@dataclass(frozen=True, order=True)
class CustomerOrder(object):
    id: int = field(compare=False)
    value: float = field(compare=True)
    product: str = field(compare=False)



__test__ = {
    'CustomerOrder': '''
        >>> order = CustomerOrder(1, 150., "cheese")
        >>> order2 = CustomerOrder(2, 10., "more cheese")
        >>> orders = [order, order2]
        >>> orders.sort()
        >>> orders
        [CustomerOrder(id=2, value=10.0, product='more cheese'), CustomerOrder(id=1, value=150.0, product='cheese')]
    '''
}


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)