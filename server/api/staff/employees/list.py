from server.api.base import BaseAPIView


class EmployeesAPIView(BaseAPIView):

    async def get(self, _):
        return [
            {
                'id': 1,
                'username': 'john.smith',
                'first_name': 'John',
                'last_name': 'Smith',
                'patronymic': 'Yellowstone'
            }
        ]

    async def post(self, request):
        pass

    async def patch(self, request):
        pass

    async def put(self, request):
        pass

    async def delete(self, request):
        pass
