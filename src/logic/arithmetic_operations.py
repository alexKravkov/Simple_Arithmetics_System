from abc import ABC, abstractmethod

from src.infra.type_validator import TypeValidator


class ArithmeticOperation(ABC):

    @abstractmethod
    def calculate(self, num1: float, num2:float) -> float:
        ...

class Addition(ArithmeticOperation):

    def calculate(self, num1: float, num2:float) -> float:
        num1 = TypeValidator.validate_numeric(num1)
        num2 = TypeValidator.validate_numeric(num2)
        return num1 + num2

class Subtraction(ArithmeticOperation):

    def calculate(self, num1: float, num2:float) -> float:
        num1 = TypeValidator.validate_numeric(num1)
        num2 = TypeValidator.validate_numeric(num2)
        return num1 - num2

class Multiplication(ArithmeticOperation):

    def calculate(self, num1: float, num2:float) -> float:
        num1 = TypeValidator.validate_numeric(num1)
        num2 = TypeValidator.validate_numeric(num2)
        return num1 * num2

class Division(ArithmeticOperation):

    def calculate(self, num1: float, num2:float) -> float:
        num1 = TypeValidator.validate_numeric(num1)
        num2 = TypeValidator.validate_numeric(num2)
        if num2 == 0:
            raise ValueError("Can't divide by zero.")
        return num1 / num2

