from sanic import Sanic
from sanic.log import logger
from sanic.response import json, text, html

from .config import config

app = Sanic()
app.config.update(**config)


@app.route("/")
async def hello(request):
    logger.info("Here is your info")
    logger.warning("Here is your warning")
    logger.error("Here is your error")
    return json({"hello": "world"})


@app.route("/json")
def post_json(request):
    return json({
        "received": True,
        "message": request.json,
    })


@app.route("/query_string")
def query_string(request):
    return json({
        "parsed": True,
        "args": request.args,
        "url": request.url,
        "query_string": request.query_string,
    })


@app.route("/files")
def post_json(request):
    test_file = request.files.get("test")

    file_parameters = {
        "body": len(test_file.body),
        "name": test_file.name,
        "type": test_file.type,
    }

    return json({
        "received": True,
        "file_names": request.files.keys(),
        "test_file_parameters": file_parameters,
    })


@app.route("/form")
def post_json(request):
    return json({
        "received": True,
        "form_data": request.form,
        "test": request.form.get("test"),
    })


@app.route("/users", methods=["POST", ])
def create_user(request):
    return text(
        "You are trying to create a user with the following POST: %s"
        % request.body
    )


@app.route('/text')
def handle_request(request):
    return text('Hello world!')


@app.route('/html')
def handle_request(request):
    return html('<h1>Hello world!</h1>')


@app.route('/json_extends')
def handle_request(request):
    return json(
        {'message': 'Hello world!'},
        headers={'X-Served-By': 'sanic'},
        status=200
    )


if __name__ == "__main__":
    app.run(**app.config.SANIC_RUN)
