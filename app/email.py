from app import app
from flask_mail import Message
from app import mail
from flask import render_template
from app.forms import ContactForm
from threading import Thread

def send_async_email(app, msg):
  with app.app_context():
    mail.send(msg)

def send_email():
  form = ContactForm()
  context = {
    "form": form,
    "google_maps_api_key": app.config["GOOGLE_MAPS_API_KEY"],
    "name": form.name.data,
    "email": form.email.data,
    "phone": form.phone.data,
    "subject": form.subject.data,
    "message": form.message.data,
  }
  msg = Message(
    subject="[Zara Consulting] New inquiry",
    sender=f"Zara Consulting <{app.config['COMPANY_EMAIL']}>",
    recipients=[f"{app.config['PRES_EMAIL']}"],
    html=render_template('email/mail.html', **context)
  )
  # mail.send(msg)
  Thread(target=send_async_email, args=(app, msg)).start()

  # return requests.post(
  #   app.config['MAIL_DOMAIN'],
  #   auth=("api", app.config['MAIL_API_KEY']),
  #   data={
  #     "from": f"Zara Consulting <{app.config['COMPANY_EMAIL']}>",
  #     "to": [f"{app.config['PRES_EMAIL']}"],
  #     "subject": f"[Zara Consulting] New inquiry",
  #     "html": render_template('email/mail.html', **context)
  #   }
  # )