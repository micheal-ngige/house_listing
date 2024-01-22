from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username= db.Column(db.String(50), unique= True, nullable= False)
    password = db.Column(db.String(100), nullable= False)

    def serialiaze(self):
        return{
            'id':self.id,
            'username':self.username,
            'password':self.password
        }