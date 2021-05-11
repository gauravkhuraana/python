import pytest

@pytest.fixture
def sum2Nbrs():
 def sum(a,b):
    return a+b
 return sum   
