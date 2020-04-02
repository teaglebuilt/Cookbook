import pytest

class A(object):
    def show(self, msg):
        print(f"class A -- msg: {msg}")

class B(object):
    def show(self, msg):
        print(f"class B -- msg: {msg}")

class C(object):
    def show(self, msg):
        print(f"class C -- msg: {msg}")


def test_polymorphism():
    objs = [A(), B(), C(), A()]
    for idx, obj in enumerate(objs):
        msg = f"message # {idx + 1}"
        obj.show(msg)


if __name__ == '__main__':
    test_polymorphism()
