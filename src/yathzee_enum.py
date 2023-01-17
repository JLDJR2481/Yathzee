from src.dies import Dies


class Yatzy_enum:

    def __init__(self, *dice):
        self.dice = list(dice)

    @staticmethod
    def ones(*dices):
        ONE = Dies.ONE.value
        return dices.count(ONE) * ONE

    @staticmethod
    def twos(*dices):
        TWO = Dies.TWO.value
        total_twos = dices.count(TWO)
        return total_twos * TWO

    @staticmethod
    def threes(*dices):
        THREE = Dies.THREE.value
        return dices.count(THREE) * THREE

    def fours(self):
        FOUR = Dies.FOUR.value
        return self.dice.count(FOUR) * 4

    def fives(self):
        total = 0
        FIVE = Dies.FIVE.value
        for i in self.dice:
            if i == FIVE:
                total += i

        return total

    def sixes(self):
        total = 0
        SIX = Dies.SIX.value
        for i in self.dice:
            if i == SIX:
                total += i
        return total

    @staticmethod
    def chance(*dice):
        score = 0
        for i in dice:
            score += i
        return score

    @staticmethod
    def yatzy(*dice):
        if dice.count(dice[0]) == 5:
            return 50
        else:
            return 0

    @staticmethod
    def pair(*dices):
        number_with_pair = 0
        dices = sorted(dices)
        for i in dices:
            if dices.count(i) == 2:
                if i > number_with_pair:
                    number_with_pair += i
        return number_with_pair * 2

    @staticmethod
    def doublePair(*dices):
        first_pair = 0
        second_pair = 0
        dices = sorted(dices)
        for i in dices:
            if dices.count(i) == 2:
                if first_pair == 0:
                    first_pair += i

                elif second_pair == 0 and first_pair != i:
                    second_pair += i
        return ((first_pair + second_pair) * 2)

    @staticmethod
    def threeOfaKind(*dices):
        for i in dices:
            if dices.count(i) >= 3:
                return i * 3
        return 0

    @staticmethod
    def fourOfaKind(*dices):
        for i in dices:
            if dices.count(i) == 4:
                return i * 4
        return 0

    @staticmethod
    def fullHouse(*dices):
        number_pair = 0
        number_three = 0
        for i in dices:
            if dices.count(i) != 2 and dices.count(i) != 3:
                return 0
            else:
                if dices.count(i) == 2:
                    if number_pair == 0:
                        number_pair += i
                elif dices.count(i) == 3:
                    if number_three == 0:
                        number_three += i
        return (number_pair * 2 + number_three * 3)

    @staticmethod
    def largeStraight(*dices):
        if sorted(dices) == list(range(min(dices), max(dices)+1)):
            return sum(dices)
        else:
            return 0

    @staticmethod
    def smallStraight(*dices):
        dices = sorted(dices)
        straightLst = []
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
