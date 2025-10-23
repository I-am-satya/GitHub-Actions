# app.py
# This is a test commit
#This is a test commit 2
def add(a, b, c):
    return a + b + c

def test_add():
    assert add(1, 2, 3) == 6
    assert add(1, -1, 0) == 0
