from Units import Quantity
from os.path import join, dirname
from yaml import load
from nose.tools import assert_almost_equal, assert_true, assert_raises

Examples = load(open(join(dirname(__file__), 'examples.yml')))

Metre=Quantity(1, ['metre'], [1])
Kilometre=Quantity(1000,['metre'],[1])
Second=Quantity(1,['second'],[1])
Minute=Quantity(60, ['second'],[1])

NewMinute=60*Second.convert('second','minute',0.0166666666666666666666666666666666666666666666666666)
def test_equality():
    assert_true(1000*Metre==Kilometre)

def test_conversion_number():
    assert_almost_equal(NewMinute.number,1.0)

def test_conversion_units():
    assert_true(NewMinute.units==['minute'])         

def test_addition():
    with assert_raises(TypeError):
        Metre+Second