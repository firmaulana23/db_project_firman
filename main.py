from flask import Flask
from program.http.api import api_bp
from common.database import db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://new_user:password@localhost/db_project_firman'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

# Import and register blueprints
app.register_blueprint(api_bp)

if __name__ == '__main__':
    app.run(debug=True)