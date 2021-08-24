import pytest


@pytest.mark.xfail
@pytest.mark.greatnum
def test_grt():
   num = 1000
   assert num > 1000


@pytest.mark.xfail
@pytest.mark.greatnum
def test_grt_equal():
   num = 1000
   assert num >= 1000


@pytest.mark.skip
@pytest.mark.small
def test_small():
   num = 1000
   assert num < 2000


@pytest.mark.small
def test_small_equal():
   num = 2000
   assert num == 2000