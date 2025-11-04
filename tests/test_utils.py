import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.utils import add_numbers


def test_add_numbers():
    assert add_numbers(2, 3) == 5
