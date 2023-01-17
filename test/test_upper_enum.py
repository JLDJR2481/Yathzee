from src.yathzee_enum import Yatzy_enum
import pytest

# Tests para la parte Upper de la tabla de Yahtzee

# Test para Ace en Upper Section


@pytest.mark.aces_enum
def test_one_enum():
    assert 1 == Yatzy_enum.ones(1, 2, 3, 4, 5)
    assert 2 == Yatzy_enum.ones(1, 1, 5, 4, 2)
    assert 4 == Yatzy_enum.ones(1, 2, 1, 1, 1)

# Test para Twoes en Upper Section


@pytest.mark.twos_enum
def test_two_enum():
    assert 2 == Yatzy_enum.twos(2, 1, 6, 4, 5)
    assert 6 == Yatzy_enum.twos(2, 2, 6, 5, 2)
    assert 4 == Yatzy_enum.twos(2, 2, 5, 3, 1)

# Test para Threes en Upper Section


@pytest.mark.threes_enum
def test_three_enum():
    assert 9 == Yatzy_enum.threes(5, 6, 3, 3, 3)
    assert 3 == Yatzy_enum.threes(3, 6, 4, 5, 1)
    assert 6 == Yatzy_enum.threes(3, 3, 6, 4, 5)

# Test para Fours en Upper Section


@pytest.mark.fours_enum
def test_four_enum():
    assert 16 == Yatzy_enum(4, 6, 4, 4, 4).fours()
    assert 4 == Yatzy_enum(4, 6, 5, 1, 1).fours()
    assert 8 == Yatzy_enum(5, 6, 1, 4, 4).fours()

# Test para Fives en Upper Section


@pytest.mark.fives_enum
def test_five_enum():
    assert 10 == Yatzy_enum(5, 5, 1, 3, 6).fives()
    assert 15 == Yatzy_enum(5, 5, 1, 6, 5).fives()
    assert 5 == Yatzy_enum(5, 1, 2, 6, 3).fives()

# Test para Sixes en Upper Section


@pytest.mark.sixes_enum
def test_six_enum():
    assert 6 == Yatzy_enum(6, 2, 5, 1, 1).sixes()
    assert 18 == Yatzy_enum(6, 4, 6, 1, 6).sixes()
    assert 12 == Yatzy_enum(6, 2, 1, 4, 6).sixes()
