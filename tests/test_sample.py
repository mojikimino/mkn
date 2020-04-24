from mkn import sample


def test_work_well():
    expected = "ok"
    result = sample.work_well()
    assert result == expected

def test_say_hello():
    expected = "hello"
    result = sample.say_hello()
    assert result == expected
