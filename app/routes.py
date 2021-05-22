from flask import render_template, redirect, url_for, current_app as app
from app.forms import ContactForm
from app.email import send_contact_email

@app.route('/')
def index():
  context = {'form': ContactForm()}
  return render_template('index.html', **context)

@app.route('/contact', methods=['POST'])
def contact():
  form = ContactForm()
  data = {
      "form": form,
      "name": form.name.data,
      "email": form.email.data,
      "phone": form.phone.data,
      "subject": form.subject.data,
      "message": form.message.data,
    }
  if form.validate_on_submit():
    send_contact_email(data)
  return redirect(url_for('index'))