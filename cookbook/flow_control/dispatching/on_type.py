""" Dispatching on Type"""


class Shape:  # pylint: disable=too-few-public-methods
    """ parent type class """

    def __init__(self, solid):
        self.solid = solid


class Circle(Shape):  # pylint: disable=too-few-public-methods
    """ subclass of type shape """

    def __init__(self, center, radius, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.center = center
        self.radius = radius


class Parallelogram(Shape):   # pylint: disable=too-few-public-methods
    """ subclass of type shape """

    def __init__(self, pa, pb, pc, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._pa = pa
        self._pb = pb
        self._pc = pc


def draw_circle(shape):
    # pylint: disable=missing-function-docstring
    print("\u25CF" if shape.solid else "\u25A1")


def draw_parallelogram(shape):
    # pylint: disable=missing-function-docstring
    print("\u25B2" if shape.solid else "\u25B3")


def draw(shape):
    # pylint: disable=missing-function-docstring
    if isinstance(shape, Circle):
        draw_circle(shape)
    elif isinstance(shape, Parallelogram):
        draw_parallelogram(shape)
    else:
        raise TypeError("Cannot draw shape {!r}".format(shape))


def main():
    """ execute """
    shapes = [
        Circle(center=(0, 0), radius=5, solid=False),
        Parallelogram(pa=(0, 0), pb=(2, 0), pc=(1, 1), solid=False),
    ]
    for shape in shapes:
        draw(shape)


if __name__ == "__main__":
    main()
