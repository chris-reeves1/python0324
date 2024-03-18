from pytest_files.my_functions import *
import pytest

# pytest widely test.
# plain assert statements.
# flexibility/integration - run against unittest.
# automatic test detection. 
# fixtures - sets certain conditions + paramatisation - pass through diff sets of data. 

def  test_answer():
    result = add(1, 2)
    assert add(1, 2) == 1 + 2
    assert add(1, 2) == 3
    assert add(-1, -1) == -2
    assert add(0, 0) == 0
    assert add(10000, 20000) == 30000
    assert result == 3

def test_divide():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

# class-based test

#class test_area:

    #def set_up_method(self):
     #   self.x = Area(5,10)

    #def teardown_method(self):
     #   del self.x

    #def test_area(self):
        #assert self.x.area_calc() == 50

# fixtures:

@pytest.fixture
def x():
    return Area(10, 5)

def test_x(x):
    assert x.area_calc() == 50

# paramatisation

@pytest.mark.parametrize("width, length, area", [(5, 10, 50), (10, 10, 100), (1, 10, 10)])
def test_multiple_areas(width, length, area):
    x = Area(width, length)
    assert x.area_calc() == area


#@pytest.mark.skip(reason="something")
@pytest.mark.xfail(reason="broken")
def test_answer_b():
    assert add(1, 2) == 3



