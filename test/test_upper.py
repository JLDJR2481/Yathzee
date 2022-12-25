from src.yathzee import Yathzee
import pytest
# Tests para la parte Upper de la tabla de Yahtzee


# Test para Ace en Upper Section


def test_one():
    assert 1 == Yathzee.ones(1, 2, 3, 4, 5)
    assert 2 == Yathzee.ones(1, 1, 5, 4, 2)
    assert 4 == Yathzee.ones(1, 2, 1, 1, 1)

# Test para Twoes en Upper Section


def test_two():
    assert 2 == Yathzee.twos(2, 1, 6, 4, 5)
    assert 6 == Yathzee.twos(2, 2, 6, 5, 2)
    assert 4 == Yathzee.twos(2, 2, 5, 3, 1)

# Test para Threes en Upper Section


def test_three():
    assert 9 == Yathzee.threes(5, 6, 3, 3, 3)
    assert 3 == Yathzee.threes(3, 6, 4, 5, 1)
    assert 6 == Yathzee.threes(3, 3, 6, 4, 5)

# Test para Fours en Upper Section


def test_four():
    assert 16 == Yathzee.fours(4, 6, 4, 4, 4)
    assert 4 == Yathzee.fours(4, 6, 5, 1, 1)
    assert 8 == Yathzee.fours(5, 6, 1, 4, 4)

# Test para Fives en Upper Section


def test_five():
    assert 10 == Yathzee.fives(5, 5, 1, 3, 6)
    assert 15 == Yathzee.fives(5, 5, 1, 6, 5)
    assert 5 == Yathzee.fives(5, 1, 2, 6, 3)

# Test para Sixes en Upper Section


def test_six():
    assert 6 == Yathzee.sixes(6, 2, 5, 1, 1)
    assert 18 == Yathzee.sixes(6, 4, 6, 1, 6)
    assert 12 == Yathzee.sixes(6, 2, 1, 4, 6)
