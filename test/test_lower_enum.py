from src.yathzee_enum import Yatzy_enum
import pytest


@pytest.mark.pairs_enum
def test_pair_enum():
    assert 6 == Yatzy_enum.pair(3, 1, 5, 2, 3)
    assert 12 == Yatzy_enum.pair(6, 1, 6, 4, 2)
    assert 10 == Yatzy_enum.pair(5, 2, 4, 6, 5)
    assert 2 == Yatzy_enum.pair(1, 1, 5, 3, 4)


@pytest.mark.double_pairs_enum
def test_doublePair_enum():
    assert 6 == Yatzy_enum.doublePair(2, 2, 1, 1, 6)
    assert 22 == Yatzy_enum.doublePair(6, 6, 5, 5, 1)
    assert 20 == Yatzy_enum.doublePair(6, 6, 4, 4, 1)
    assert 8 == Yatzy_enum.doublePair(3, 3, 1, 1, 2)


@pytest.mark.three_of_a_kind_enum
def test_threeOfaKind_enum():
    assert 3 == Yatzy_enum.threeOfaKind(1, 1, 1, 5, 4)
    assert 6 == Yatzy_enum.threeOfaKind(2, 2, 1, 5, 2)
    assert 18 == Yatzy_enum.threeOfaKind(6, 1, 2, 6, 6)
    assert 15 == Yatzy_enum.threeOfaKind(5, 1, 2, 5, 5)
    assert 0 == Yatzy_enum.threeOfaKind(1, 1, 6, 5, 4)


@pytest.mark.four_of_a_kind_enum
def test_fourOfaKind_enum():
    assert 8 == Yatzy_enum.fourOfaKind(1, 2, 2, 2, 2)
    assert 4 == Yatzy_enum.fourOfaKind(1, 1, 5, 1, 1)
    assert 24 == Yatzy_enum.fourOfaKind(6, 6, 6, 6, 1)
    assert 20 == Yatzy_enum.fourOfaKind(5, 5, 1, 5, 5)
    assert 0 == Yatzy_enum.fourOfaKind(2, 2, 2, 1, 4)


@pytest.mark.full_house_enum
def test_fullHouse_enum():
    assert 16 == Yatzy_enum.fullHouse(4, 4, 4, 2, 2)
    assert 0 == Yatzy_enum.fullHouse(4, 4, 1, 1, 2)
    assert 18 == Yatzy_enum.fullHouse(6, 6, 2, 2, 2)
    assert 21 == Yatzy_enum.fullHouse(5, 3, 5, 3, 5)


@pytest.mark.small_straight_enum
def test_smallStraight_enum():
    assert 16 == Yatzy_enum.smallStraight(1, 2, 3, 6, 4)
    assert 0 == Yatzy_enum.smallStraight(1, 6, 5, 4, 2)
    assert 16 == Yatzy_enum.smallStraight(6, 4, 2, 3, 1)
    assert 0 == Yatzy_enum.smallStraight(6, 5, 4, 3, 1)


@pytest.mark.large_straight_enum
def test_largeStraight_enum():
    assert 15 == Yatzy_enum.largeStraight(1, 2, 3, 4, 5)
    assert 0 == Yatzy_enum.largeStraight(6, 1, 3, 2, 4)
    assert 20 == Yatzy_enum.largeStraight(6, 5, 4, 3, 2)
    assert 0 == Yatzy_enum.largeStraight(1, 5, 4, 2, 6)


@pytest.mark.yatzhee_enum
def test_yatzhee_enum():
    assert 50 == Yatzy_enum.yatzy(6, 6, 6, 6, 6)
    assert 0 == Yatzy_enum.yatzy(4, 4, 4, 2, 4)
    assert 0 == Yatzy_enum.yatzy(1, 5, 4, 6, 2)
    assert 50 == Yatzy_enum.yatzy(4, 4, 4, 4, 4)


@pytest.mark.chance_enum
def test_chance_enum():
    assert 10 == Yatzy_enum.chance(4, 3, 1, 1, 1)
    assert 15 == Yatzy_enum.chance(2, 5, 1, 3, 4)
    assert 18 == Yatzy_enum.chance(6, 2, 1, 5, 4)
