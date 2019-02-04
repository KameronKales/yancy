from flask import Blueprint
routes = Blueprint('routes', __name__)

from .usage import *
from .spam import *
