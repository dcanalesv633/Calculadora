import pytest
from operaciones import suma

def test_suma():
    assert suma(2, 2) == 4


@pytest.mark.parametrize(
        "input_a, input_b, expected",
        [
            (3,2,5),
            (2,3,5),
            (suma(3,2),5,10),
            (3, suma(2,5),10),
            (7,3,10),
            (3,7,10),
            (7,8,14)
        ]
)
def test_suma_multi(input_a, input_b, expected):
    assert suma(input_a, input_b) == expected

#https://www.youtube.com/watch?v=5ufpsjfk99U