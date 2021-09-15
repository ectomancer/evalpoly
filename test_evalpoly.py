import evalpoly

def test_evalpoly():
    """pytest test data, test data by kgryte @github.com
    Test data MIT License Copyright (c) 2016 The Compute.io Authors."""
    assert evalpoly.evalpoly([], 10) == 0
    assert evalpoly.evalpoly([1], 10) == 1
    assert evalpoly.evalpoly([3, 2, 1], 0) == 3
    assert evalpoly.evalpoly([4, 5], 6) == 34
    assert evalpoly.evalpoly((-4, -5), 6) == -34
    assert evalpoly.evalpoly((-19, 7, -4, 6), 3) == 128
