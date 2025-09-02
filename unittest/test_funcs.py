from basic_func import evn, avg, max, min

def test_evn():
    assert evn(2) == True
    assert evn(1) == False
    assert evn(8) == True
    assert evn(3) == False

def test_avg():
    assert avg(2, 4) == 3
    assert avg(1, 5) == 3
    assert avg(3, 7) == 5
    assert avg(4, 8) == 6

def test_max():
    assert max(2, 4) == 4
    assert max(1, 5) == 5
    assert max(3, 7) == 7
    assert max(4, 8) == 8

def test_min():
    assert min(2, 4) == 2
    assert min(1, 5) == 1
    assert min(3, 7) == 3
    assert min(4, 8) == 4