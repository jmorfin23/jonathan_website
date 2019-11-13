from flask import Flask
from flask_bootstrap import Bootstrap
from flask_admin import Admin
from config import Config
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


#flask
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

#bootstrap
bootstrap = Bootstrap(app)



from app import routes, models
