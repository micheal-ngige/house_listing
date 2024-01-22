from app.models.house_model import House
from flask  import request, jsonify
from app import db
from sqlalchemy.exc import SQLAlchemyError
import logging



logging.basicConfig(level=logging.INFO)
def handle_error(e, status_code):
     logging.error(str(e))
     return jsonify({'error' : str(e)}), status_code

def create_house():
     try:
          data = request.get_json()

          if 'housetype' not in data or 'location' not in data or 'price' not in data or 'description' not in data or 'user_id' not in data or 'review_id' not in data:
            
               return handle_error('missing data fields', 400)
          new_house= House(housetype=data['housetype'],location=data['location'],price=data['price'],description=data['description'],user_id=data['user_id'], review_id=data['review_id'])
        
          db.session.add(new_house)
          db.session.commit()
          return 'house created successfully'
          
     except SQLAlchemyError as e:
          return handle_error(e, 400)

