from sanic import Blueprint
from sanic.response import text, json

bp = Blueprint("v1_req", url_prefix="/req", version="v1")


@bp.get("/")
def index(request):
    return text(f"Hello, here is {request.url}")


@bp.get("/json")
def post_json(request):
    return json({
        "received": True,
        "message": request.json,
    })


@bp.get("/query_string")
def query_string(request):
    return json({
        "parsed": True,
        "args": request.args,
        "url": request.url,
        "query_string": request.query_string,
    })


@bp.get("/files")
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


@bp.get("/form")
def post_json(request):
    return json({
        "received": True,
        "form_data": request.form,
        "test": request.form.get("test"),
    })


@bp.post("/users")
def create_user(request):
    return text(
        "You are trying to create a user with the following POST: %s"
        % request.body
    )
