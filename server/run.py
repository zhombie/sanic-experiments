import settings
from api import build_api_blueprint
from core.json import json
from core.web.engine.app import App
from core.web.engine.request import APIRequest
from di.di import di

app = App(
    'sample',
    dumps=json.dumps,
    loads=json.loads,
    request_class=APIRequest
)

app.config.DEBUG = False
app.config.FALLBACK_ERROR_FORMAT = 'json'


@app.before_server_start
async def before_server_start(_app, _loop):
    await di.db.connect(
        host=settings.DATABASE_HOST,
        port=settings.DATABASE_PORT,
        user=settings.DATABASE_USER,
        password=settings.DATABASE_PASSWORD,
        database=settings.DATABASE_NAME,
        min_size=1,
        max_size=10
    )


@app.before_server_stop
async def before_server_stop(_app, _loop):
    await di.db.disconnect()

    di.destroy()


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
