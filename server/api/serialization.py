import time
import traceback
from functools import wraps

from core.web.engine.request import APIRequest
from core.web.engine.response import APIResponse


def on_api_request(func):
    @wraps(func)
    async def wrapper(request: APIRequest, *args, **kwargs) -> APIResponse:
        print('on_api_request() ->', func, request, args, kwargs)

        a = time.perf_counter()

        try:
            d = await func(request, *args, **kwargs)
        except Exception as exc:
            traceback.print_exc()

            k = False
            d = {}
            e = {
                'c': exc.__class__.__name__,
                'm': str(exc),
                'x': getattr(exc, 'context') or {} if hasattr(exc, 'context') else {}
            }
        else:
            k = True
            e = {}

        b = time.perf_counter()

        return APIResponse.json(
            {
                'm': {
                    'r': request.to_dict(),
                    't': (b - a) * 1000
                },
                'k': k,
                'd': d,
                'e': e
            },
            status=kwargs.get('status', 200)
        )

    return wrapper
