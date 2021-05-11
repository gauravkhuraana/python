import pytest

def test_useFixture(sum):
    print("The sum is",sum)


def test_2NbrsAddViaFixture(sum2Nbrs):
    print("The sume of numbers is", sum2Nbrs(2,4))
