

class ShippingContainer:
    """class attribute"""
    next_serial = 1337

    def __init__(self, owner_code, contents):
        """instance attribute"""
        self.owner_code = owner_code
        self.contents = contents
        self.serial = ShippingContainer.next_serial
        ShippingContainer.next_serial += 1


# ShippingContainer(33, "something")
