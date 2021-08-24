import pytest


@pytest.mark.div
def test_divisible_by_5(value):
   assert value % 5 == 0


@pytest.mark.div
def test_divisible_by_12(value):
   assert value % 12 == 0