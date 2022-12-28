class Yathzee:

    @staticmethod
    def __init__(self,  *dices):
        self.dices = list(dices)

# Funciones para Upper sections
    @staticmethod
    def ones(*dices):
        amount = dices.count(1)
        return amount * 1

    @staticmethod
    def twos(*dices):
        amount = dices.count(2)
        return amount * 2

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

# Funciones para lower sections

    @staticmethod
    def pair(*dices):
        counter = 0
        for i in dices:
            if dices.count(i) == 2:
                counter += i
        return counter

    @staticmethod
    def doublePair(*dices):
        counter = 0
        for i in dices:
            if dices.count(i) == 2:
                counter += i
        return counter

    @staticmethod
    def threeOfaKind(*dices):
        counter = 0
        for i in dices:
            if dices.count(i) == 3:
                counter += i
        return counter

    @staticmethod
    def fourOfaKind(*dices):
        counter = 0
        for i in dices:
            if dices.count(i) == 4:
                counter += i
        return counter

    @staticmethod
    def fullHouse(*dices):
        pair = False
        threeOfaKind = False
        dices = sorted(dices, reverse=True)
        for i in dices:
            if dices.count(i) == 2:
                pair = True
            elif dices.count(i) == 3:
                threeOfaKind = True
        if pair and threeOfaKind:
            return 25
        else:
            return 0

    @staticmethod
    def smallStraight(*dices):
        straightLst = []
        dices = sorted(dices)
        for i in dices:
            if i == dices[0]:
                straightLst.append(i)
                continue
            elif i != dices[0]:
                if i == straightLst[-1] + 1:
                    straightLst.append(i)
        if len(straightLst) == 4:
            return 30
        return 0

    @staticmethod
    def largeStraight(*dices):
        if sorted(dices) == list(range(min(dices), max(dices)+1)):
            return 40
        else:
            return 0

    @staticmethod
    def yathzee(*dices):
        for i in dices:
            if dices.count(i) == 5:
                return 50
            else:
                return 0

    @staticmethod
    def chance(*dices):
        counter = 0
        for i in dices:
            counter += i
        return counter
