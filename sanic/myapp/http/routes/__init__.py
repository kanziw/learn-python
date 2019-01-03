from sanic import Blueprint

from .v1 import bp_v1

routes = Blueprint.group(bp_v1)
