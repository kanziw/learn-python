from sanic import Sanic
from sanic.log import logger
from sanic.response import json

from .config import config

app = Sanic()
app.config.update(**config)


@app.route('/')
async def hello(request):
    logger.info('Here is your info')
    logger.warning('Here is your warning')
    logger.error('Here is your error')
    return json({'hello': 'world'})


if __name__ == '__main__':
    app.run(**app.config.SANIC_RUN)
