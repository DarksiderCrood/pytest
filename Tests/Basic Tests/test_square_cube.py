import pytest
import math


@pytest.mark.square
def test_sqroot():  # this will run
   num = 9
   assert math.sqrt(num) == 3 # pass with dot . sign

@pytest.mark.square
def testsquarenum(): # this will run
   num = 71
   assert 71*71 == 401 # failed with sign F

def tescompare(): # this will not run as test is not mentioned in function name
   assert 122 == 112

@pytest.mark.cube
def test_cubenum(): # this will run
    num = 3
    assert 3**3 == 27 # pass with dot . sign

# To Run This Code
'''
Complete code without verbose: pytest
Complete code with verbose: pytest -v
'''

# Note − pytest and pytest -v command will execute all the files of format test_* or *_test in 
#        the current directory and subdirectories.