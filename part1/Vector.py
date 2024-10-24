from math import hypot


class Vector(object):

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __add__(self, other: "Vector") -> "Vector":
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        raise TypeError(f"类型错误{type(other)}")

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __abs__(self):
        return hypot(self.x, self.y)

    def __mul__(self, scalar: int):
        return Vector(self.x * scalar, self.y * scalar)


def main():
    v1 = Vector(2, 4)
    v2 = Vector(2, 1)
    v3 = v1 + v2
    print(abs(v3))


if __name__ == "__main__":
    main()
