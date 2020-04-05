from mkn import sample


def test_say():
    expected = "say"
    result = sample.say()
    assert result == expected
