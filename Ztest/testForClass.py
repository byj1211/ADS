from dataclasses import dataclass


@dataclass
class A:
    x: float
    y: float

    def __eq__(self, other):
        return self.x + self.y == other.x + other.y


if __name__ == '__main__':
    item = A(5, 3)
    item2 = A(4, 4)

    print(item, item2, item2 == item)
