from sanic import Blueprint
from sanic.response import text

bp = Blueprint("v1_param", url_prefix="/param", version="v1")


@bp.get("/")
def index(request):
    return text(f"Hello, here is {request.url}")


@bp.get('/user/<user_id:int>')
def handle_request(request, user_id):
    return text(f'Hello {user_id}!')


@bp.get('/user/<user_name:[0-9][A-z]+>')
def handle_request(request, user_name):
    return text(f'Hello int+{user_name}!')


@bp.get('/user/<user_name>')
def handle_request(request, user_name):
    return text(f'Hello {user_name}!')
