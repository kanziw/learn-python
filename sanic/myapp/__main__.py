from sanic import Sanic
from sanic.response import json

from .config import config

app = Sanic()
app.config.update(**config)


@app.route('/')
async def hello(request):
    return json({'hello': 'world'})


if __name__ == '__main__':
    app.run(**app.config.SANIC_RUN)
