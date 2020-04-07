from mkn import sample


def test_say():
    expected = "ok"
    result = sample.work_well()
    assert result == expected
