from hello import greet


def test_greet_world():
    assert greet("world") == "Hello, world!"


def test_greet_alice():
    assert greet("Alice") == "Hello, Alice!"
