""" Dispatching on Type"""
from functools import singledispatch


class Shape:
    """ parent type class """
    # pylint: disable=too-few-public-methods

    def __init__(self, solid):
        self.solid = solid


class Circle(Shape):
    """ subclass of type shape """
    # pylint: disable=too-few-public-methods

    def __init__(self, center, radius, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.center = center
        self.radius = radius


class Parallelogram(Shape):
    """ subclass of type shape """
    # pylint: disable=too-few-public-methods

    def __init__(self, pa, pb, pc, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._pa = pa
        self._pb = pb
        self._pc = pc


class Triangle(Shape):
    """ subclass of type shape """
    # pylint: disable=too-few-public-methods

    def __init__(self, pa, pb, pc, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._pa = pa
        self._pb = pb
        self._pc = pc


@singledispatch
def draw(shape):
    """ bind resulting wrapper to the name of the original function"""
    raise TypeError("Dont know how to draw {!r}".format(shape))


@draw.register(Circle)
def _(shape):
    # pylint: disable=missing-function-docstring
    print("\u25CF" if shape.solid else "\u25A1")


@draw.register(Parallelogram)
def _(shape):
    # pylint: disable=missing-function-docstring
    print("\u25B2" if shape.solid else "\u25B3")


@draw.register(Triangle)
def _(shape):
    # pylint: disable=missing-function-docstring
    print("\u25B2" if shape.solid else "\u25B3")


def main():
    """ calls draw function which will select the specific overload or fall back
    to default implementation"""

    shapes = [
        Circle(center=(0, 0), radius=5, solid=False),
        Parallelogram(pa=(0, 0), pb=(2, 0), pc=(1, 1), solid=False),
        Triangle(pa=(0, 0), pb=(1, 2), pc=(2, 0), solid=True)
    ]
    for shape in shapes:
        draw(shape)


if __name__ == "__main__":
    main()
