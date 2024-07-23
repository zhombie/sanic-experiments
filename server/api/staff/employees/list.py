from dataclasses import dataclass
from typing import Optional

from sanic_ext import validate

from api.base import BaseAPIView
from api.validation import is_valid_str


@dataclass
class EmployeeCreateParams:
    username: str
    first_name: str
    last_name: Optional[str] = None
    patronymic: Optional[str] = None

    def __post_init__(self):
        self.username = self.username.strip()
        self.first_name = self.first_name.strip()
        self.last_name = self.last_name.strip() if self.last_name else None

        assert is_valid_str(self.username, min_length=2, max_length=100)
        assert is_valid_str(self.first_name, min_length=2, max_length=100)
        if self.last_name:
            assert is_valid_str(self.last_name, min_length=2, max_length=100)


class EmployeesAPIView(BaseAPIView):

    async def get(self, _):
        print('EmployeesAPIView#get()')
        return [
            {
                'id': 1,
                'username': 'john.smith',
                'first_name': 'John',
                'last_name': 'Smith',
                'patronymic': 'Yellowstone'
            }
        ]

    @validate(json=EmployeeCreateParams)
    async def post(self, _, body: EmployeeCreateParams):
        print('EmployeesAPIView#post() -> body:', body)
        return {
            'id': 1,
            'username': 'john.smith',
            'first_name': 'John',
            'last_name': 'Smith',
            'patronymic': 'Yellowstone'
        }

    async def patch(self, request):
        pass

    async def put(self, request):
        pass

    async def delete(self, request):
        pass
