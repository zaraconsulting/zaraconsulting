from app import app
from flask import render_template, redirect, url_for

@app.context_processor
def get_info():
  return dict(
    company_email=app.config['COMPANY_EMAIL'],
    company_phone=app.config['COMPANY_PHONE'],
    company_name_short="Zara Consulting",
    company_name_long="Zara Consulting, Inc.",
  )

@app.route('/')
def index():
  return render_template('index.html')

