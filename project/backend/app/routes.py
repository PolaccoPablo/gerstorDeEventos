from app import app
from app.controllers import user_bp, event_bp           

#regristrar los blueprints 
app.register_blueprint(user_bp, url_prefix='/users')
app.register_blueprint(event_bp, url_prefix='/events')
