from datetime import datetime
from email.message import EmailMessage
import smtplib
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///personal_website.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# Email (Gmail SMTP). Credentials come from .env; MAIL_PASSWORD must be a
# Gmail App Password, not the account's normal password.
app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER', 'smtp.gmail.com')
app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT', '587'))
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['CONTACT_RECIPIENT'] = os.getenv('CONTACT_RECIPIENT', 'dibyaranjan.official@gmail.com')

db = SQLAlchemy(app)


def send_contact_email(name, email, message):
    """Email a contact-form submission to CONTACT_RECIPIENT.

    Returns True on success, False if sending failed or SMTP is not configured.
    """
    username = app.config['MAIL_USERNAME']
    # Gmail displays App Passwords as four space-separated groups; the real
    # password is the 16 characters with spaces removed.
    password = (app.config['MAIL_PASSWORD'] or '').replace(' ', '')
    if not username or not password:
        app.logger.warning('Contact email not sent: MAIL_USERNAME/MAIL_PASSWORD not set.')
        return False

    msg = EmailMessage()
    msg['Subject'] = f'New contact form message from {name}'
    msg['From'] = username
    msg['To'] = app.config['CONTACT_RECIPIENT']
    msg['Reply-To'] = email
    msg.set_content(
        f'Name: {name}\n'
        f'Email: {email}\n\n'
        f'Message:\n{message}\n'
    )

    try:
        with smtplib.SMTP(app.config['MAIL_SERVER'], app.config['MAIL_PORT']) as server:
            server.starttls()
            server.login(username, password)
            server.send_message(msg)
        return True
    except Exception as exc:  # noqa: BLE001 - log and fall back gracefully
        app.logger.error('Failed to send contact email: %s', exc)
        return False

class ContactMessage(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

@app.context_processor
def inject_current_year():
    return {'current_year': datetime.utcnow().year}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        if not name or not email or not message:
            flash('Please fill in all fields.', 'field empty')
            return redirect(url_for('contact'))

        contact_message = ContactMessage(name=name, email=email, message=message)
        db.session.add(contact_message)
        db.session.commit()

        send_contact_email(name, email, message)

        flash('Thanks for your message! I will get back to you soon.', 'success')
        return redirect(url_for('contact'))

    return render_template('contact.html')

# Create tables at import so they exist under any WSGI server (e.g. gunicorn
# on Render), not only when this file is run directly.
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
