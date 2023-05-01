from dataclasses import dataclass
from typing import Optional


@dataclass
class APIException:
    message: Optional[str] = None

    def __iter__(self):
        return self.message

    def __dict__(self) -> dict:
        return {
            'message': self.message or 'Undefined'
        }


class ValidationException(APIException):
    message = 'Validation Exception'
