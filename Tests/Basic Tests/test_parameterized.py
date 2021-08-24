import pytest


@pytest.mark.parametrize("num, output",[(1,3),(2,6),(3,8),(4,12)])
def test_parametrize_1(num, output):
   assert 3*num == output