def div_by(n, d):
    """ n and d are ints > 0
        Return True if d divides n evenly and False otherwise """
    return n % d == 0
def test_div_by(): 
    assert div_by(6, 3) == True
    assert div_by(7, 3) == False
    assert div_by(10, 5) == True
    assert div_by(10, 4) == False
    assert div_by(1, 1) == True