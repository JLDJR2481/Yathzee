class Yathzee:

    @staticmethod
    def __init__(self, *dices):
        self.dices = list(dices)

# Funciones para Upper sections
    @staticmethod
    def ones(*dices):
        amount = dices.count(1)
        return amount * 1

    @staticmethod
    def twos(*dices):
        total = dices.count(2)
        return total * 2

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
        dices = sorted(dices)
        for i in dices:
            if dices.count(i) == 2:
                if i != counter:
                    counter = 0
                    counter += i
        return counter * 2

    @staticmethod
    def doublePair(*dices):
        actualPairs = []
        dices = sorted(dices)
        for i in dices:
            if dices.count(i) >= 2:
                if i not in actualPairs:
                    actualPairs.append(i)

        if len(actualPairs) == 2:
            return (sum(actualPairs) * 2)
        else:
            return 0

    @staticmethod
    def threeOfaKind(*dices):
        counter = 0
        die = 0
        for i in dices:
            if dices.count(i) >= 3 and counter < 3:
                counter += 1
                if die == 0:
                    die += i

        return die * counter

    @staticmethod
    def fourOfaKind(*dices):
        counter = 0
        die = 0
        for i in dices:
            if dices.count(i) >= 4 and counter < 4:
                counter += 1
                if die == 0:
                    die += i
        return counter * die

    @staticmethod
    def fullHouse(*dices):
        pair = False
        threeOfaKind = False
        dices = sorted(dices, reverse=True)
        amount = 0
        for i in dices:
            amount += i
            if dices.count(i) == 2:
                pair = True
            elif dices.count(i) == 3:
                threeOfaKind = True

        if pair and threeOfaKind:
            return amount
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
        if len(straightLst) >= 4:
            return sum(dices)
        return 0

    @staticmethod
    def largeStraight(*dices):
        if sorted(dices) == list(range(min(dices), max(dices)+1)):
            return sum(dices)
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


if __name__ == "__main__":
    #assert 12 == Yathzee(4, 4, 4, 5, 5).fours()
    #assert 10 == Yathzee(4, 4, 4, 5, 5).fives()
    assert 18 == Yathzee(6, 5, 6, 6, 5).sixes()
