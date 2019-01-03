from sanic import Sanic
from sanic.log import logger
from sanic.response import json

from .config import config
from .http.routes import routes

app = Sanic()
app.config.update(**config)


@app.route("/")
async def index(request):
    logger.info("Here is your info")
    logger.warning("Here is your warning")
    logger.error("Here is your error")
    return json({"hello": "world"})


app.blueprint(routes)

if __name__ == "__main__":
    app.run(**app.config.SANIC_RUN)
