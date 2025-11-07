#addition
now = datetime.now()
print("Date and time when test case run ")
print(now.strftime("%Y-%m-%d %H:%M:%S))
                   
def add(a, b):
    return a + b

def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0
