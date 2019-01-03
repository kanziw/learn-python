from sanic import Blueprint
from sanic.response import text, json, html

bp = Blueprint("v1_res", url_prefix="/res", version="v1")


@bp.get("/")
def index(request):
    return text(f"Hello, here is {request.url}")


@bp.route('/text')
def handle_request(request):
    return text('Hello world!')


@bp.route('/html')
def handle_request(request):
    return html('<h1>Hello world!</h1>')


@bp.route('/json_extends')
def handle_request(request):
    return json(
        {'message': 'Hello world!'},
        headers={'X-Served-By': 'sanic'},
        status=200
    )
