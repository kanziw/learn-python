from sanic import Blueprint

from .param import bp as bp_param
from .req import bp as bp_req
from .res import bp as bp_res

bp_v1 = Blueprint.group(bp_req, bp_res, bp_param)
