from app.models.user import User
from app import db

def add_user(user):
    db.session.add(user)
    db.session.commit()
    
def det_user_by_username(username):
    return User.query.filter_by(username=username).frist()

    
