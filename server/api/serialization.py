import traceback
from functools import wraps

from core.web.engine.exception import BadRequest
from core.web.engine.request import APIRequest
from core.web.engine.response import APIResponse


def on_api_request(func):
    @wraps(func)
    async def wrapper(request: APIRequest, *args, **kwargs) -> APIResponse:
        print('on_api_request() ->', func, request, args, kwargs)

        try:
            response = await func(request, *args, **kwargs)
        except Exception as e:
            traceback.print_exc()
            raise BadRequest(message=str(e))

        return APIResponse.json(
            {
                'meta': {
                    'request': request.to_dict()
                },
                'data': response
            },
            status=kwargs.get('status', 200)
        )

    return wrapper
