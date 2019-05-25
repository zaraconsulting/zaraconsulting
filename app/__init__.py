from flask import Flask
app = Flask(__name__)

from config import Config
app.config.from_object(Config)

from flask_mail import Mail
mail = Mail(app)

from app import routes, models