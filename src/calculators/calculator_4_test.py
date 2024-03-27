from typing import Dict, List
from pytest import raises

import numpy

from src.calculators.calculator_4 import Calculator4

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

class MockDriverHandler:
    def average(self, body: Dict) -> float:
        return 5.75


def test_average():
    mock_request = MockRequest({"numbers": [10, 5, 5, 3]})
    calculator_4 = Calculator4(MockDriverHandler())

    response = calculator_4.calculate(mock_request)

    assert response == {'data': {'Calculator': 4, 'Success': True, 'value': 5.75}}


def test_average_with_body_error():
    mock_request = MockRequest(body={"something": 1})
    calculator_4 = Calculator4(MockDriverHandler())

    with raises(Exception) as excinfo:
        calculator_4.calculate(mock_request)

    assert str(excinfo.value) == "body mal formatado!"

