from flask import Blueprint

bp = Blueprint('bp', __name__)


@bp.route('/')
def home():
    return '<h1>Home</h1>'
