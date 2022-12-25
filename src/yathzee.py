class Yathzee:

    @staticmethod
    def __init__(self,  *dices):
        self.dices = list(dices)

    @staticmethod
    def ones(*dices):
        amount = dices.count(1)
        return amount * 1

    @staticmethod
    def twos(*dices):
        sum = dices.count(2)
        return sum * 2

    @staticmethod
    def threes(*dices):
        return (dices.count(3) * 3)

    @staticmethod
    def fours(*dices):
        count = 0
        for i in dices:
            if i == 4:
                count += 4
        return count

    @staticmethod
    def fives(*dices):
        return dices.count(5) * 5

    @staticmethod
    def sixes(*dices):
        amount = 0
        for i in dices:
            if i == 6:
                amount += 1

        return amount * 6
