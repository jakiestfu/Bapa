import os
from flask import Flask, url_for
from flask_mail import Mail
from datetime import date

app = Flask(__name__)

app.config.update(
    DEBUG = True,
    SECRET_KEY = os.environ['bapa_session_secret'],

    MAIL_SERVER = os.environ['bapa_mail_server'],
    MAIL_PORT = os.environ['bapa_mail_port'],
    MAIL_USERNAME = os.environ['bapa_mail_username'],
    MAIL_PASSWORD = os.environ['bapa_mail_password'],
    MAIL_DEFAULT_SENDER = os.environ['bapa_mail_sender'],

    USHPA_CHAPTER = os.environ['bapa_ushpa_chapter'],
    USHPA_PIN = os.environ['bapa_ushpa_pin']
)

mail = Mail(app)

from bapa.modules import home, account, password # blueprints

# Template Globals
app.jinja_env.globals['year'] = date.today().year

app.register_blueprint(home.home_bp)
app.register_blueprint(account.acct_bp, url_prefix='/account')
app.register_blueprint(password.pass_bp, url_prefix='/password')
