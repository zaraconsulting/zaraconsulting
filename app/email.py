import requests
from flask import render_template, current_app as app
from app.forms import ContactForm

def send_email():
  form = ContactForm()
  context = {
    "form": form,
    # "google_maps_api_key": app.config["GOOGLE_MAPS_API_KEY"],
    "name": form.name.data,
    "email": form.email.data,
    "phone": form.phone.data,
    "subject": form.subject.data,
    "message": form.message.data,
  }
  return requests.post(
    app.config['MAIL_DOMAIN'],
    auth=("api", app.config['MAIL_API_KEY']),
    data={
      "from": f"Zara Consulting <{app.config['COMPANY_EMAIL']}>",
      "to": [f"{app.config['MAIL_ACCOUNT']}"],
      "subject": f"[Zara Consulting] New inquiry",
      "html": render_template('email/mail.html', **context)
    }
  )