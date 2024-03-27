from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from flask import request as FlaskRequest
from typing import Dict, List
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError


class Calculator4:

    def __init__(self, driver_handler: DriverHandlerInterface):
        self.__driver_handler = driver_handler

    def calculate(self, request: FlaskRequest) -> Dict:
        body = request.json
        input_data = self.__validate_body(body)
        average = self.__calculate_average(input_data)
        formated_response = self.__format_response(average)
        return formated_response

    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise HttpUnprocessableEntityError("body mal formatado!")
        input_data = body["numbers"]
        return input_data

    def __calculate_average(self, numbers: List[float]) -> float:
        average = self.__driver_handler.average(numbers)
        return average

    def __format_response(self, average: float) -> Dict:
        return {
            "data": {
                "Calculator": 4,
                "value": average,
                "Success": True
            }
        }
