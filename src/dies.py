from enum import Enum, unique


@unique
class Dies(Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6

    @classmethod
    def values(cls):
        return [number._value_ for number in Dies.__members__.values()]

    @classmethod
    def reversedValues(cls):
        return reversed(cls.values())


if __name__ == "__main__":
    print(list(Dies))
    print(Dies(1))

    print(Dies['ONE'])

    print(Dies.ONE)

    print(Dies.ONE.name)

    print(Dies.ONE.value)

    for number in Dies.__members__.values():
        print(number._value_)

    print(Dies.values())

    print(Dies.reversedValues())
