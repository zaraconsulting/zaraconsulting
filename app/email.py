from flask import render_template, current_app as app
from app.forms import ContactForm
from flask_mail import Message
from app import mail

# def send_email():
#   form = ContactForm()
#   context = {
#     "form": form,
#     # "google_maps_api_key": app.config["GOOGLE_MAPS_API_KEY"],
#     "name": form.name.data,
#     "email": form.email.data,
#     "phone": form.phone.data,
#     "subject": form.subject.data,
#     "message": form.message.data,
#   }
#   return requests.post(
#     app.config['MAIL_DOMAIN'],
#     auth=("api", app.config['MAIL_API_KEY']),
#     data={
#       "from": f"Zara Consulting <{app.config['COMPANY_EMAIL']}>",
#       "to": [f"{app.config['MAIL_ACCOUNT']}"],
#       "subject": f"[Zara Consulting] New inquiry",
#       "html": render_template('email/mail.html', **context)
#     }
#   )

def send_email(subject, sender, recipients, html_body, reply_to=None, bcc=None):
    msg = Message(subject, sender=sender, recipients=recipients, reply_to=reply_to, bcc=bcc)
    msg.html = html_body
    print(msg.html)
    mail.send(msg)

def send_contact_email(form_data):
  # print(form_data)
  send_email(
    f'[{app.config.get("COMPANY_NAME_SHORT")}] Contact Form Inquiry', 
    sender='noreply@zaraconsulting.org',
    reply_to=form_data.get('email'),
    bcc=app.config.get('ADMIN'), 
    recipients=[app.config.get('MAIL_USERNAME')],
    html_body=render_template('email/mail.html', **form_data)
  )