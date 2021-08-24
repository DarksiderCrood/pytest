import pytest


@pytest.mark.div
def test_divisible_by_4(value):
   assert value % 4 == 0


@pytest.mark.div
def test_divisible_by_2(value):
   assert value % 2 == 0