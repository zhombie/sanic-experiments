from orjson import dumps

from api import build_api_blueprint
from core.web.engine.app import App
from core.web.engine.request import APIRequest

app = App(
    'sample',
    dumps=dumps,
    request_class=APIRequest
)

app.blueprint(build_api_blueprint())

if __name__ == '__main__':
    app.run(
        host='127.0.0.1',
        port=8000,

        access_log=False,
        debug=False,
        dev=False,

        auto_reload=True,

        workers=1,
    )
