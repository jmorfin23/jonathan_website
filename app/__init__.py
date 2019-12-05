from flask import Flask
from flask_bootstrap import Bootstrap
from flask_admin import Admin
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
from flask_cors import CORS


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
admin = Admin(app)
mail = Mail(app)


#CORS
CORS(app)

#bootstrap
bootstrap = Bootstrap(app)



from app import routes, models
