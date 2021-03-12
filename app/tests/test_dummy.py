import pytest


@pytest.fixture
def setup() -> None:
    print('setup')


def test_foo(setup):
    assert True
