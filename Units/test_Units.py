from Units import Quantity
from os.path import join, dirname
from yaml import load
from nose.tools import assert_almost_equal, assert_true, assert_raises

Examples = load(open(join(dirname(__file__), 'examples.yml')))

Metre=eval(Examples['Metre'])
Kilometre=eval(Examples['Kilometre'])
Second=eval(Examples['Second'])
Minute=eval(Examples['Minute'])
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
        
def test_number():
    with assert_raises(TypeError):
        Quantity('a',['metre'], [1])
        
def test_convert():
    with assert_raises(LookupError):
        Second.convert('metre','minute',1)
    
def test_multiply():
    assert_true(Metre*Second==Second*Metre)