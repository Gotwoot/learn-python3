'''
pip install pytest
pytest pytest_test.py
'''
# test_example.py

def add(x, y):
    return x + y

def test_addition():
    assert add(1, 2) == 3

def test_subtraction():
    assert add(5, 3) == 8
