from src.yathzee import Yathzee
import pytest

# Tests para la parte Upper de la tabla de Yahtzee

# Test para Ace en Upper Section


@pytest.mark.aces
def test_one():
    assert 1 == Yathzee.ones(1, 2, 3, 4, 5)
    assert 2 == Yathzee.ones(1, 1, 5, 4, 2)
    assert 4 == Yathzee.ones(1, 2, 1, 1, 1)

# Test para Twoes en Upper Section


@pytest.mark.twos
def test_two():
    assert 2 == Yathzee.twos(2, 1, 6, 4, 5)
    assert 6 == Yathzee.twos(2, 2, 6, 5, 2)
    assert 4 == Yathzee.twos(2, 2, 5, 3, 1)

# Test para Threes en Upper Section


@pytest.mark.threes
def test_three():
    assert 9 == Yathzee.threes(5, 6, 3, 3, 3)
    assert 3 == Yathzee.threes(3, 6, 4, 5, 1)
    assert 6 == Yathzee.threes(3, 3, 6, 4, 5)

# Test para Fours en Upper Section


@pytest.mark.fours
def test_four():
    assert 16 == Yathzee(4, 6, 4, 4, 4).fours()
    assert 4 == Yathzee(4, 6, 5, 1, 1).fours()
    assert 8 == Yathzee(5, 6, 1, 4, 4).fours()

# Test para Fives en Upper Section


@pytest.mark.fives
def test_five():
    assert 10 == Yathzee(5, 5, 1, 3, 6).fives()
    assert 15 == Yathzee(5, 5, 1, 6, 5).fives()
    assert 5 == Yathzee(5, 1, 2, 6, 3).fives()

# Test para Sixes en Upper Section


@pytest.mark.sixes
def test_six():
    assert 6 == Yathzee(6, 2, 5, 1, 1).sixes()
    assert 18 == Yathzee.sixes(6, 4, 6, 1, 6).sixes()
    assert 12 == Yathzee.sixes(6, 2, 1, 4, 6).sixes()
