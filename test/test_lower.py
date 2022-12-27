from src.yathzee import Yathzee
import pytest


@pytest.mark.pairs
def test_pair():
    assert 6 == Yathzee.pair(3, 1, 5, 2, 3)
    assert 12 == Yathzee.pair(6, 1, 6, 4, 2)
    assert 10 == Yathzee.pair(5, 2, 4, 6, 5)
    assert 2 == Yathzee.pair(1, 1, 5, 3, 4)


@pytest.mark.double_pairs
def test_doublePair():
    assert 6 == Yathzee.doublePair(2, 2, 1, 1, 6)
    assert 22 == Yathzee.doublePair(6, 6, 5, 5, 1)
    assert 20 == Yathzee.doublePair(6, 6, 4, 4, 1)
    assert 8 == Yathzee.doublePair(3, 3, 1, 1, 2)


@pytest.mark.three_of_a_kind
def test_threeOfaKind():
    assert 3 == Yathzee.threeOfaKind(1, 1, 1, 5, 4)
    assert 6 == Yathzee.threeOfaKind(2, 2, 1, 5, 2)
    assert 18 == Yathzee.threeOfaKind(6, 1, 2, 6, 6)
    assert 15 == Yathzee.threeOfaKind(5, 1, 2, 5, 5)
    assert 0 == Yathzee.threeOfaKind(1, 1, 6, 5, 4)


@pytest.mark.four_of_a_kind
def test_fourOfaKind():
    assert 8 == Yathzee.fourOfaKind(1, 2, 2, 2, 2)
    assert 4 == Yathzee.fourOfaKind(1, 1, 5, 1, 1)
    assert 24 == Yathzee.fourOfaKind(6, 6, 6, 6, 1)
    assert 20 == Yathzee.fourOfaKind(5, 5, 1, 5, 5)
    assert 0 == Yathzee.fourOfaKind(2, 2, 2, 1, 4)


@pytest.mark.full_house
def test_fullHouse():
    assert 25 == Yathzee.fullHouse(4, 4, 4, 2, 2)
    assert 0 == Yathzee.fullHouse(4, 4, 1, 1, 2)
    assert 25 == Yathzee.fullHouse(6, 6, 2, 2, 2)
    assert 25 == Yathzee.fullHouse(5, 3, 5, 3, 5)


@pytest.mark.small_straight
def test_smallStraight():
    assert 30 == Yathzee.smallStraight(1, 2, 3, 6, 4)
    assert 0 == Yathzee.smallStraight(1, 6, 5, 4, 2)
    assert 30 == Yathzee.smallStraight(6, 4, 2, 3, 1)
    assert 0 == Yathzee.smallStraight(6, 5, 4, 3, 1)


@pytest.mark.large_straight
def test_largeStraight():
    assert 40 == Yathzee.largeStraight(1, 2, 3, 4, 5)
    assert 0 == Yathzee.largeStraight(6, 1, 3, 2, 4)
    assert 40 == Yathzee.largeStraight(6, 5, 4, 3, 2)
    assert 0 == Yathzee.largeStraight(1, 5, 4, 2, 6)


@pytest.mark.yatzhee
def test_yathzee():
    assert 50 == Yathzee.yathzee(6, 6, 6, 6, 6)
    assert 0 == Yathzee.yathzee(4, 4, 4, 2, 4)
    assert 0 == Yathzee.yathzee(1, 5, 4, 6, 2)
    assert 50 == Yathzee.yathzee(4, 4, 4, 4, 4)


@pytest.mark.chance
def test_chance():
    assert 10 == Yathzee.chance(4, 3, 1, 1, 1)
    assert 15 == Yathzee.chance(2, 5, 1, 3, 4)
    assert 18 == Yathzee.chance(6, 2, 1, 5, 4)
