from functools import wraps

from core.engine import APIRequest, APIResponse


def on_api_request(func):
    @wraps(func)
    async def wrapper(request: APIRequest, *args, **kwargs) -> APIResponse:
        print(func, request, args, kwargs)

        body = {
            'meta': {
                'request': request.to_dict()
            }
        }

        response = await func(request, *args, **kwargs)

        body['data'] = response

        return APIResponse.json(
            body,
            status=kwargs.get('status', 200)
        )

    return wrapper
