from app.models.review_model import Review
from flask import request, jsonify
from app import db
from sqlalchemy.exc import SQLAlchemyError
import logging


logging.basicConfig(level=logging.INFO)

def handle_error(e, status_code):
    logging.error(str(e))
    return jsonify({'error' : str(e)}), status_code

def create_review():
    try:
        data = request.get_json()

        if 'comment' not in data :
            return handle_error("missing data fields", 400)
        new_review= Review(comment=data['comment'])
        db.session.add(new_review)
        db.session.commit()
        return 'review added successfully'

    except SQLAlchemyError as e:
        return handle_error(e, 400)      