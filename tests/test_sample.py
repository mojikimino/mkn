from mkn import sample
from mkn import downloader
from mkn import print_resources


def test_work_well():
    expected = "ok"
    result = sample.work_well()
    assert result == expected

def test_say_hello():
    expected = "hello"
    result = sample.say_hello()
    assert result == expected

def test_print_resources():
    expected = "ok"
    downloader.download()
    result = print_resources.check()
    assert result == expected
