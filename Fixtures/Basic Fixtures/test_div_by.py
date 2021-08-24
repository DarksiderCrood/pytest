import pytest


@pytest.fixture
def inp_val():
   input = 15
   return input

def test_divisible_by_5(inp_val):
   assert inp_val % 5 == 0


def test_divisible_by_2(inp_val):
   assert inp_val % 2 == 0

'''
Here, we have a fixture function named inp_val, which supplies the input to the tests. 
To access the fixture function, the tests have to mention the fixture name as input parameter.

Pytest while the test is getting executed, will see the fixture name as input parameter. 
It then executes the fixture function and the returned value is stored to the input parameter, 
which can be used by the test.
'''

# Run tests with string match: pytest -k divisible -v