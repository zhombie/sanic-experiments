from orjson import dumps

from api import build_api_blueprint
from api.home import build_home_blueprint
from core.engine import APIRequest, App

app = App(
    'sample',
    dumps=dumps,
    request_class=APIRequest
)

app.blueprint(build_home_blueprint())
app.blueprint(build_api_blueprint())

if __name__ == '__main__':
    app.run()
