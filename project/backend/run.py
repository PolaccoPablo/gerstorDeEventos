from app import app, db
import routes
# Crear las tablas en la base de datos

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)