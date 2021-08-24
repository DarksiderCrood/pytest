import pytest


@pytest.mark.greater
def test_greaternum():
   num = 1000
   assert num > 1000

@pytest.mark.greater
def test_greaternum_equal():
   num = 1000
   assert num >= 1000

@pytest.mark.less
def test_lessnum():
   num = 1000
   assert num < 2000