from src.yathzee import *


def test_chance_scores_sum_of_all_dice():
    expected = 15
    actual = Yathzee.chance(2, 3, 4, 5, 1)
    assert expected == actual
    assert 16 == Yathzee.chance(3, 3, 4, 5, 1)


def test_Yathzee_scores_50():
    expected = 50
    actual = Yathzee.yathzee(4, 4, 4, 4, 4)
    assert expected == actual
    assert 50 == Yathzee.yathzee(6, 6, 6, 6, 6)
    assert 0 == Yathzee.yathzee(6, 6, 6, 6, 3)


def test_1s():
    assert Yathzee.ones(1, 2, 3, 4, 5) == 1
    assert 2 == Yathzee.ones(1, 2, 1, 4, 5)
    assert 0 == Yathzee.ones(6, 2, 2, 4, 5)
    assert 4 == Yathzee.ones(1, 2, 1, 1, 1)


def test_2s():
    assert 4 == Yathzee.twos(1, 2, 3, 2, 6)
    assert 10 == Yathzee.twos(2, 2, 2, 2, 2)


def test_threes():
    assert 6 == Yathzee.threes(1, 2, 3, 2, 3)
    assert 12 == Yathzee.threes(2, 3, 3, 3, 3)


def test_fours_test():
    assert 12 == Yathzee(4, 4, 4, 5, 5).fours()
    assert 8 == Yathzee(4, 4, 5, 5, 5).fours()
    assert 4 == Yathzee(4, 5, 5, 5, 5).fours()


def test_fives():
    assert 10 == Yathzee(4, 4, 4, 5, 5).fives()
    assert 15 == Yathzee(4, 4, 5, 5, 5).fives()
    assert 20 == Yathzee(4, 5, 5, 5, 5).fives()


def test_sixes_test():
    assert 0 == Yathzee(4, 4, 4, 5, 5).sixes()
    assert 6 == Yathzee(4, 4, 6, 5, 5).sixes()
    assert 18 == Yathzee(6, 5, 6, 6, 5).sixes()


def test_one_pair():
    assert 6 == Yathzee.pair(3, 4, 3, 5, 6)
    assert 10 == Yathzee.pair(5, 3, 3, 3, 5)
    assert 12 == Yathzee.pair(5, 3, 6, 6, 5)


def test_two_Pair():
    assert 16 == Yathzee.doublePair(3, 3, 5, 4, 5)
    assert 18 == Yathzee.doublePair(3, 3, 6, 6, 6)
    assert 0 == Yathzee.doublePair(3, 3, 6, 5, 4)


def test_three_of_a_kind():
    assert 9 == Yathzee.threeOfaKind(3, 3, 3, 4, 5)
    assert 15 == Yathzee.threeOfaKind(5, 3, 5, 4, 5)
    assert 9 == Yathzee.threeOfaKind(3, 3, 3, 3, 5)


def test_four_of_a_knd():
    assert 12 == Yathzee.fourOfaKind(3, 3, 3, 3, 5)
    assert 20 == Yathzee.fourOfaKind(5, 5, 5, 4, 5)
    assert 12 == Yathzee.fourOfaKind(3, 3, 3, 3, 3)
    assert 0 == Yathzee.fourOfaKind(3, 3, 3, 2, 1)


def test_smallStraight():
    assert 15 == Yathzee.smallStraight(1, 2, 3, 4, 5)
    assert 15 == Yathzee.smallStraight(2, 3, 4, 5, 1)
    assert 0 == Yathzee.smallStraight(1, 2, 2, 4, 5)


def test_largeStraight():
    assert 20 == Yathzee.largeStraight(6, 2, 3, 4, 5)
    assert 20 == Yathzee.largeStraight(2, 3, 4, 5, 6)
    assert 0 == Yathzee.largeStraight(1, 2, 2, 4, 5)


def test_fullHouse():
    assert 18 == Yathzee.fullHouse(6, 2, 2, 2, 6)
    assert 0 == Yathzee.fullHouse(2, 3, 4, 5, 6)
