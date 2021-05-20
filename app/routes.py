from flask import render_template, redirect, url_for, current_app as app
from app.forms import ContactForm
from app.email import send_email

@app.route('/')
def index():
  context = {'form': ContactForm()}
  return render_template('index.html', **context)

@app.route('/contact', methods=['POST'])
def contact():
  form = ContactForm()
  if form.validate_on_submit():
    send_email()
  return redirect(url_for('index'))