import inc_dec

def test_increment():
    assert inc_dec.increment(3) == 4
    assert inc_dec.increment(-1) == 0
    assert inc_dec.increment(0) == 1
    assert inc_dec.increment(-5) == -4
    
def test_decrement():
    assert inc_dec.decrement(3) == 2
    assert inc_dec.decrement(-1) == -2
    assert inc_dec.decrement(0) == -1
    assert inc_dec.decrement(1) == 0

def test_factorial():
    assert inc_dec.factorial(0) == 1  # 0! = 1
    assert inc_dec.factorial(1) == 1  # 1! = 1
    assert inc_dec.factorial(2) == 2  # 2! = 2
    assert inc_dec.factorial(3) == 6  # 3! = 6
    assert inc_dec.factorial(4) == 24  # 4! = 24