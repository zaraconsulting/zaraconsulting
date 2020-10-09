import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config:
  FLASK_APP = os.environ.get('FLASK_APP') or os.getenv('FLASK_APP')
  FLASK_ENV = os.environ.get('FLASK_ENV') or os.getenv('FLASK_ENV')
  SECRET_KEY = os.environ.get('SECRET_KEY') or os.getenv('SECRET_KEY')
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  GOOGLE_MAPS_API_KEY = os.environ.get("GOOGLE_MAPS_API_KEY") or os.getenv("GOOGLE_MAPS_API_KEY")
  PRES_EMAIL = os.environ.get('PRES_EMAIL') or os.getenv('PRES_EMAIL')
  NOREPLY_EMAIL = os.environ.get('NOREPLY_EMAIL') or os.getenv('NOREPLY_EMAIL')
  COMPANY_EMAIL = os.environ.get('COMPANY_EMAIL') or os.getenv('COMPANY_EMAIL')
  COMPANY_PHONE = os.environ.get('COMPANY_PHONE') or os.getenv('COMPANY_PHONE')
  MAIL_API_KEY = os.environ.get('MAIL_API_KEY') or os.getenv('MAIL_API_KEY')
  MAIL_DOMAIN = os.environ.get('MAIL_DOMAIN') or os.getenv('MAIL_DOMAIN')
  IMAGE_FOLDER = os.path.join(basedir, 'app/blueprints/blog/static/uploads')
  MAIL_ACCOUNT = os.environ.get('MAIL_ACCOUNT') or os.getenv('MAIL_ACCOUNT')