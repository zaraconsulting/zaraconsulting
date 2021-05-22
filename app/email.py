from flask import render_template, current_app as app
from sendgrid.helpers import mail
from app.forms import ContactForm
import sendgrid, os
from sendgrid.helpers.mail import Mail, Email, To, Content, from_email, subject

def send_email():
  form = ContactForm()

  context = {
    "form": form,
    "name": form.name.data,
    "email": form.email.data,
    "phone": form.phone.data,
    "subject": form.subject.data,
    "message": form.message.data,
  }
  sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SG_API_KEY'))
  from_email = Email(app.config.get('MAIL_ACCOUNT'))
  to_email = To(app.config.get('PRES_EMAIL'))
  subject = form.subject.data
  mail = Mail(from_email=from_email, to_emails=to_email, subject=subject, html_content=render_template('email/mail.html', **context))

  mail_json = mail.get()

  res = sg.client.mail.send.post(request_body=mail_json)

  # return requests.post(
  #   app.config['MAIL_DOMAIN'],
  #   auth=("api", app.config['MAIL_API_KEY']),
  #   data={
  #     "from": f"Zara Consulting <{app.config['COMPANY_EMAIL']}>",
  #     "to": [f"{app.config['MAIL_ACCOUNT']}"],
  #     "subject": f"[Zara Consulting] New inquiry",
  #     "html": render_template('email/mail.html', **context)
  #   }
  # )