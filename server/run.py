from orjson import dumps

from api import build_api_blueprint
from core.web.engine.app import App
from core.web.engine.request import APIRequest

app = App(
    'sample',
    dumps=dumps,
    request_class=APIRequest
)

# app.blueprint(build_home_blueprint())
app.blueprint(build_api_blueprint())

if __name__ == '__main__':
    app.run()
