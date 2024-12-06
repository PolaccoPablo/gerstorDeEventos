from app import app
from app.controllers.event_controller import  event_bp
from app.controllers.users_controller import user_bp

# Registrar los blueprints
app.register_blueprint(user_bp, url_prefix='/users')
app.register_blueprint(event_bp, url_prefix='/events')