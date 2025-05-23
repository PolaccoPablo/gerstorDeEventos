from app.repositories.user_repositoy import add_user, get_user_by_username
from app.models.user import User

def register_user(username, password):
    if get_user_by_username(username):
        return None
    new_user = User(username=username, password=password)
    add_user(new_user)
    return new_user

def authenticate_user(username, password):
    user = get_user_by_username(username)
    if user and user.password == password:
        return user
    return None

def infoUsuario(user_name):
    return get_user_by_username(user_name)


