


class SortedSet:

    def __init__(self, items=None):
        """ design list object with sorted """
        self._items = sorted(set(items)) if items is not None else []
        self.index = 0

    def __contains__(self, item):
        return item in self._items

    def __len__(self):
        return len(self._items)
