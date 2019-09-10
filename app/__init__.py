from flask import Flask
from flask_bootstrap import Bootstrap



#flask
app = Flask(__name__)



#bootstrap
bootstrap = Bootstrap(app)



from app import routes
