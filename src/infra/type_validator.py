from typing import Type, Union

from src.logic.errors import TypeVerificationError


class TypeValidator:

    @staticmethod
    def validate_numeric(value: any, expected_type: Type = float) -> Union[int, float]:
        """
        Validate and convert input to expected numeric type
        :param value: Input value to validate
        :param expected_type: Expected numeric type (int or float)
        """
        try:
            # If value is int or float, just cast to the needed numeric type
            if isinstance(value, (int, float)):
                return expected_type(value)

            # Try to convert str to numeric
            if isinstance(value, str):
                try:
                    return expected_type(value)
                except ValueError as e:
                    raise TypeVerificationError(f"Can't convert {value} to {expected_type.__name__}: {e}")
            raise TypeVerificationError(f"Invalid type. Expected numeric, got {type(value)}")
        except (ValueError, TypeError) as e:
            raise TypeVerificationError(f'Type verification failed: {e}')


