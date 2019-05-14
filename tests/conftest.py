import pytest
import os


@pytest.fixture()
def test_name():
    test_name = (os.environ.get('PYTEST_CURRENT_TEST'))
    print('CURR_TEST', test_name)
