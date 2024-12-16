import _socket
from socket import socket

from src.infra.logger import LoggerConfig
from src.infra.type_validator import TypeValidator
from src.logic.errors import TypeVerificationError


class ArithmeticsClient:

    def __init__(self, host: str = 'localhost', port: int = 65432):
        self.logger = LoggerConfig.setup_logger('ArithmeticsClient')
        self.host = host
        self.port = port


    def get_user_input(self) -> tuple[float, float, str] | None:
        self.logger.info(f"Function get_user_input Enter")
        try:
            while True:
                try:
                    num1_input = input("Enter first number: ")
                    num1 = TypeValidator.validate_numeric(num1_input)
                    break
                except TypeVerificationError as e:
                    self.logger.error(f"Invalid input: {e}")

            while True:
                try:
                    num2_input = input("Enter second number: ")
                    num2 = TypeValidator.validate_numeric(num2_input)
                    break
                except TypeVerificationError as e:
                    self.logger.error(f"Invalid input: {e}")

            valid_operations = ['+', '-', '*', '/']
            while True:
                op = input("Enter arithmetic operation ('+', '-', '*', '/'): ")
                if op in valid_operations:
                    break
                self.logger.warning("Invalid operation. Choose from +, -, *, /")
            self.logger.info(f"Function get_user_input Exit")
            return num1, num2, op
        except Exception as e:
            self.logger.error(f"Error occurred: {e}")


    def send_data_to_srv(self,num1: float, num2: float, operation: str) -> str | None:
        self.logger.info(f"Function send_data_to_srv Enter")
        try:
            with socket(_socket.AF_INET, _socket.SOCK_STREAM) as s:
                s.connect((self.host, self.port))
                request = f"{num1},{num2},{operation}"
                s.sendall(request.encode())
                res = s.recv(1024).decode()
                self.logger.info(f"Function send_data_to_srv Exit")
                return res
        except Exception as e:
            self.logger.error(f"Client error: {e}")
            return None

    def run(self):
        try:
            user_input = self.get_user_input()
            if user_input:
                res = self.send_data_to_srv(*user_input)
                if res:
                    self.logger.info(f"Result: {res}")
                    print(f"Result: {res}")
        except Exception as e:
            self.logger.error(f"Client error: {e}")

if __name__ == "__main__":
    client = ArithmeticsClient()
    client.run()
