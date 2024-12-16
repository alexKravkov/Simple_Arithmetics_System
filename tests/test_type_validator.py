import pytest

from src.infra.type_validator import TypeValidator
from src.logic.errors import TypeVerificationError


class TestTypeValidator:
    """Test suite for TypeValidator class"""

    def test_validate_numeric_float(self):
        """Test validation of float inputs"""
        assert TypeValidator.validate_numeric(5.5) == 5.5
        assert TypeValidator.validate_numeric("5.5") == 5.5

    def test_validate_numeric_int(self):
        """Test validation of integer inputs"""
        assert TypeValidator.validate_numeric(5) == 5.0
        assert TypeValidator.validate_numeric("5") == 5.0

    def test_validate_numeric_invalid_input(self):
        """Test validation of invalid inputs"""
        with pytest.raises(TypeVerificationError):
            TypeValidator.validate_numeric("abc")

        with pytest.raises(TypeVerificationError):
            TypeValidator.validate_numeric([1, 2, 3])