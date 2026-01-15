from cube_number import calculate_cube

def test_calculate_cube_positive():
    assert calculate_cube(3) == 27

def test_calculate_cube_zero():
    assert calculate_cube(0) == 0

def test_calculate_cube_negative():
    assert calculate_cube(-2) == -8

def test_calculate_cube_float():
    assert calculate_cube(2.5) == 15.625
