import _socket
from socket import socket
from typing import Union

from src.infra.logger import LoggerConfig
from src.logic.arithmetic_operations import Addition, Subtraction, Multiplication, Division
from src.logic.errors import TypeVerificationError


class ArithmeticsServer:

    def __init__(self, host: str = 'localhost', port: int = 65432):
        self.logger = LoggerConfig.setup_logger('ArithmeticsServer')
        self.host = host
        self.port = port
        self. operations = {
            '+': Addition(),
            '-': Subtraction(),
            '*': Multiplication(),
            '/': Division()
        }

    def start_server(self):
        self.logger.info(f"Function start_server Enter")
        try:
            with socket(_socket.AF_INET, _socket.SOCK_STREAM) as s:
                s.bind((self.host,self.port))
                s.listen()
                self.logger.info(f"Server listening on {self.host}:{self.port}")

                while True:
                    conn, addr = s.accept()
                    with conn:
                        self.logger.info(f"Connected with {addr}.")
                        data = conn.recv(1024).decode()
                        res = self.process_request(data)
                        conn.sendall(str(res).encode())
        except Exception as e:
            self.logger.error(f"Server error: {e}")
        self.logger.info(f"Function start_server Exit")


    def process_request(self, request: str) -> Union[float, str]:
        self.logger.info(f"Function process_request Enter")
        try:
            parts = request.split(',')
            if len(parts) != 3:
                raise TypeVerificationError(f"Invalid request format.Expected 3 values, got {len(parts)}.")
            num1 = parts[0]
            num2 = parts[1]
            op = parts[2]

            if op not in self.operations:
                raise TypeVerificationError(f"Unknown operation: {op}")
            res = self.operations[op].calculate(num1, num2)
            self.logger.info(f"Calculated {num1} {op} {num2} = {res}")
            self.logger.info(f"Function process_request Exit")
            return res
        except (TypeVerificationError, ValueError) as e:
            self.logger.error(f"Calc or TypeVerification error: {e}")
            return str(e)
        except Exception as e:
            self.logger.error(f"Unexpected error: {e}")
            return "Unexpected error"




if __name__ == "__main__":
    server = ArithmeticsServer()
    server.start_server()