from flask import Blueprint
from app.controllers.user_controller import create_user
from app.controllers.house_controller import create_house
from app.controllers.review_controller import create_review

bp = Blueprint('bp', __name__)


@bp.route('/')
def home():
    return '<h1>Home</h1>'

@bp.route('/user', methods=['POST'])
def add_user():
    return create_user()

@bp.route('/house', methods=['POST'])
def add_house():
    return create_house()

@bp.route('/review', methods=['POST'])
def add_review():
  return create_review()



  
   