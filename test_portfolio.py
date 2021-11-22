from portfolio import Portfolio
import pytest

def test_empty_portfolio():
    p = Portfolio()
    assert p.cost() == 0.0

def test_buy_one_stock():
    p = Portfolio()
    p.buy("IBM", 100, 176.48)
    assert p.cost() == 17648.0

def test_but_2_stock():
    p = Portfolio()
    p.buy("IBM", 100, 176.48)
    p.buy('HPQ', 100, 36.15)
    assert p.cost() == 21263.00

def test_not_enough_arguments_to_guy():
    p = Portfolio()
    with pytest.raises(TypeError):
        p.buy("IBM")